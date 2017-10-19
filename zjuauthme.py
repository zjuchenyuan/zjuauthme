import execjs
from EasyLogin import EasyLogin
from pprint import pprint, pformat
import json
jssrc = open("security.js","r").read()
jscontext = execjs.compile(jssrc)

__all__ = ["ZJUAUTHME"]

class ZJUAUTHME():
    AUTHME_DOMAIN = "https://zjuam.zju.edu.cn"
    def __init__(self, xh, password):
        self.xh = xh
        self.password = password
        self.status = "Not Login"
        self.a = EasyLogin()

    def _getPubKey(self):
        data = self.a.get(self.AUTHME_DOMAIN+"/cas/v2/getPubKey", o=True).json()
        return data["exponent"], data["modulus"]

    def login(self):
        global jscontext
        self.a.get(self.AUTHME_DOMAIN+"/cas/login")
        execution = self.a.b.find("input",{"name":"execution"})["value"]
        encryptedPwd = jscontext.call("main", self.password, *self._getPubKey())
        x=self.a.post_dict(self.AUTHME_DOMAIN+"/cas/login",{"username":self.xh, "password":encryptedPwd, "authcode":"", "execution":execution, "_eventId":"submit" })
        if "iPlanetDirectoryPro" in x.headers.get("set-cookie",""):
            self.status = "Login OK"
            return True
        else:
            self.status = "Login Failed"
            return False
        
    

