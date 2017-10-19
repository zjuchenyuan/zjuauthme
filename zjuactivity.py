from zjuauthme import ZJUAUTHME
import json

class ZJUActivity(ZJUAUTHME):
    DOMAIN = "http://one.zju.edu.cn"
    from cachedata import CACHE
    def _website_login(self):
        assert self.status == "Login OK"
        indexjumppage = self.a.get(self.DOMAIN+"/", o=True)
        if "taskcenter" in indexjumppage.headers.get("location",""):
            # Successful Login:
            #     'Location': 'http://one.zju.edu.cn/taskcenter/'
            x=self.a.get(indexjumppage.headers["location"], o=True)
            while x.status_code!=200:
                x=self.a.get(x.headers["location"], o=True) # follow 302 jump to finish oauth login
            return True
        else:
            return False
    
    def _get_xiaoqu(self, csrf_token=None):
        """
        csrf_token为空时返回缓存数据，否则发起Post请求查询
        其中formStepId只需指定一个"报告会、论坛、讲座活动审批"的流程ID即可，无需是自己创建的
        """
        if csrf_token is None:
            return self.CACHE["xiaoqu"]
        xiaoqu_r = self.a.post_dict(self.DOMAIN+"/infoplus/interface/suggest",{"formStepId":"408560","prefix":"","type":"Code","code":"xiaoQu","parent":"","isTopLevel":"true","pageNo":"0","rand":"","settings":"{}","csrfToken":csrf_token,"lang":"en"})
        data = [i["codeId"] for i in xiaoqu_r.json()["items"]]
        return data

    def _get_louyu(self, xiaoqu, csrf_token=None):
        """
        输入校区，查询校区包含的楼宇名称
        csrf_token为空时返回缓存数据，否则发起Post请求查询
        其中formStepId只需指定一个"报告会、论坛、讲座活动审批"的流程ID即可，无需是自己创建的
        """
        if csrf_token is None:
            return self.CACHE["xiaoqu_louyu"][xiaoqu]
        louyu_r = self.a.post_dict(self.DOMAIN+"/infoplus/interface/suggest",{"formStepId":"408560","prefix":"","type":"Code","code":"LouYu","parent":xiaoqu,"isTopLevel":"false","pageNo":"0","rand":"","settings":"{}","csrfToken":csrf_token,"lang":"en"})
        data = [i["codeId"] for i in louyu_r.json()["items"]]
        return data

    def _get_zy(self, louyu, csrf_token=None):
        """
        输入楼宇，查询该楼宇包含的资源
        csrf_token为空时返回缓存数据，否则发起Post请求查询
        其中formStepId只需指定一个"报告会、论坛、讲座活动审批"的流程ID即可，无需是自己创建的
        """
        if csrf_token is None:
            return self.CACHE["louyu_ziyuan"][louyu]
        zy_r = self.a.post_dict(self.DOMAIN+"/infoplus/interface/suggest",{"formStepId":"408560","prefix":"","type":"Code","code":"ZY","parent":louyu,"isTopLevel":"false","pageNo":"0","rand":"","settings":"{}","csrfToken":csrf_token,"lang":"en"})
        data = [(i["codeId"], i["codeName"]) for i in zy_r.json()["items"]]
        return data

    def _query(self, ziyuan_id, csrf_token):
        """
        输入资源id，输出已被占用的情况
        此函数用于实时查询，不应该在此层面配置缓存，csrf_token为必须参数
        虽然浏览器发出了60多个参数，但经过我的层层筛选 只有楼宇id是需要的
        """
        query_r = self.a.post(self.DOMAIN+"/infoplus/interface/fieldChanging","formStepId=408560&formData=%7B%22fieldSQCDZY%22%3A%22{ziyuan_id}%22%7D&fieldName=fieldSQCDbtnQuery&fieldValue=&path=&csrfToken={csrf_token}".format(**locals()))
        occupy_data = json.loads(query_r.json()["entities"][0])["occupyZY"]
        result = [] # 格式： [校区,楼宇,资源,资源id,开始时间,结束时间,资源使用情况(活动名称)]
        for item in occupy_data:
            result.append([item["occupyXQ"], item["occupyLY"],item["occupyZY"],item["occupyZYID"],item["occupyStartTime"],item["occupyEndTime"],item["occupyRemark"] ])
        return result

    def run(self):
        assert self._website_login(), "[ERROR] It seems you cannot login {domain} using your ZUINFO identity".format(domain=self.DOMAIN)
        start_page = self.a.get(self.DOMAIN+"/infoplus/form/FW_HDSQ/start",o=True)
        csrf_token = self.a.b.find("meta",{"itemscope":"csrfToken"})["content"]
        print(csrf_token)
        ziyuan_set = self.CACHE["ziyuan"]
        whole_data = []
        for ziyuan_id , ziyuan_name in ziyuan_set:
            print(ziyuan_name)
            whole_data.extend(self._query(ziyuan_id, csrf_token))
        return whole_data


