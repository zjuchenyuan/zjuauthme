from zjuactivity import ZJUActivity,Filter_ZJUActivity
import datetime
import pickle
import copy
from secret import up, zuinfo_username, zuinfo_password
import datetime
import imgkit
def html2jpg(html, filename):
    config = imgkit.config(wkhtmltoimage='./wkhtmltoimage')
    options= {
        'format': 'png',
        'transparent': None,
        'quality': 1,
    }
    imgkit.from_string(html, filename, config=config, options=options)

def data2html(data, filter=None):
    if filter is None:
        def filter(item):
            return True
    data.sort(key=lambda i:(i[4],i[0],i[1],i[2]))
    for item in data:
        t = datetime.datetime.strptime(item[4],"%Y-%m-%d %H:%M")
        if t.hour<12:
            brief = "上午"
        elif t.hour<18:
            brief = "下午"
        else:
            brief = "晚上"
        item[0], item[3], item[4], item[5] = item[0].replace("校区",""),t.strftime("%Y-%m-%d ")+brief, item[4].split(" ")[1], item[5].split(" ")[1]
    html="""<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<style>
body{
    font-family: "Microsoft YaHei" !important;
}
.updatetime{
position:absolute;
right:0px;
top:0px;
z-index:100;
 
}
</style>
<table style="table-layout:fixed; "><col width="50px"><col width="130px"><col width="110px"><col width="130px"><col width="42px"><col width="42px"><col width="480px">
<tr><th colspan=3>地点</th><th colspan=3>时间</th><th align="left" width="480px">活动名称</th></tr>
"""
    for item in data:
        if filter(item):
            if "下午" in item[3]:
                style="background-color: #DDD"
            else:
                style=""
            html+="<tr style='%s'><td>%s</td></tr>"%(style, "</td><td>".join(item))
    html+="</table>"
    html+="""
<pre>
Author: chenyuan; Code: https://github.com/zjuchenyuan/zjuauthme; Data Source: http://one.zju.edu.cn
请注意活动不一定存在/欢迎你去，请自行确认活动详情; 此数据源也并不能给出所有活动信息
</pre>
<div class="updatetime"><pre>数据更新时间：%s</pre></div>"""%(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    return html

def main():
    x = Filter_ZJUActivity(zuinfo_username, zuinfo_password)
    x.login()
    _data = x.run()
    
    # Today
    data = copy.deepcopy(_data)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    filter_today=lambda item:today in item[3]    
    html_today = data2html(data, filter_today)
    open("test1.html","w").write(html_today)
    html2jpg(html_today,"zjuactivity_today.png")
    up.put("/zjuactivity_today.png", open("zjuactivity_today.png","rb"))
    
    # Tomorrow
    data = copy.deepcopy(_data)
    tomorrow = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    filter_tomorrow=lambda item: tomorrow in item[3]
    html_tomorrow = data2html(data, filter_tomorrow)
    open("test2.html","w").write(html_tomorrow)
    html2jpg(html_tomorrow,"zjuactivity_tomorrow.png")
    up.put("/zjuactivity_tomorrow.png", open("zjuactivity_tomorrow.png","rb"))
    
    # Purge CDN cache
    up.purge(["/zjuactivity_today.png", "/zjuactivity_tomorrow.png"], domain="api.py3.io")

if __name__ == "__main__":
    main()