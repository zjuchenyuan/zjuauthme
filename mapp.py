from EasyLogin import EasyLogin
import json, re
from pprint import pprint


class MAPP():
    def __init__(self, username, password, phonename="iPhone", imei="666666"):
        self.a=EasyLogin()
        self.imei = imei
        a = self.a
        x = a.post("http://mids.zju.edu.cn/_ids_mobile/login18_9",
               {"username":username, "password":password, 
                "name":phonename, "deviceName":phonename, "serialNo": imei,
                "code":"2", "apnsKey":"1104a89792cc321fb2f", "appName":"teacher"
               })
        assert x.status_code == 200
        for item in json.loads(x.headers['ssoCookie']):
            if item["cookieName"] not in ["_csrf", "_pc0", "_pv0", "_pf0"]:
                #print(item['cookieName'], item['cookieValue'], item['cookieDomain'], item['cookiePath'])
                a.s.cookies.set(item['cookieName'], item['cookieValue'], domain=item['cookieDomain'], path=item['cookiePath']) 
        x = a.post("http://mids.zju.edu.cn/_ids_mobile/loginedUser15", "")
        data = x.json()["data"]
        self.data = data

    def openpay(self, uxid=None, userid=None):
        a = self.a
        x = a.post("http://mapp.zju.edu.cn/_web/_lightapp/pay/api/code.rst", {"code":self.imei})
        #print(x.headers)
        data = {s.split("'")[1]: s.split("'")[-1] for s in re.findall(r"name='[^']+' value='[^']+", x.text)}
        x = a.post("http://ecardpay.zju.edu.cn:9001/ThirdWeb/AuthPayCodeLocal", data)
        assert x.headers["Location"] == "/ThirdWeb/PayCode"
        return self.pay_barcode()
    
    def pay_barcode(self):
        x = self.a.post("http://ecardpay.zju.edu.cn:9001/ThirdWeb/GetBarCode", 'acctype=001&json=true')
        return x.json()["Obj"]
    
    def card_detail(self):
        x = self.a.get("http://mapp.zju.edu.cn/lightapp/lightapp/getCardDetail", o=True)
        return x.json()["data"]["query_card"]["card"][0]
    
    def card_balance(self, account):
        x = self.a.get("http://mapp.zju.edu.cn/lightapp/lightapp/getCardBalance", params={"account":account}, o=True)
        #print(x.text)
        return x.json()["data"]["query_accinfo"]["accinfo"][0]
    
    

if __name__ == "__main__":
    x = MAPP(input("username:"), input("password:"))
    print(x.data)
    print(x.card_balance(x.card_detail()["account"]))
    print(x.openpay())
    