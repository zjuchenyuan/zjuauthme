# zjuauthme & zjuactivity
Login ZJU Unified Identity Authentication system using Python3

## ZJU Activity

* 登录统一通行证 [Code](zjuauthme.py) 依赖：[execjs](https://pypi.python.org/pypi/PyExecJS) [EasyLogin](https://github.com/zjuchenyuan/EasyLogin)
* 爬取[http://one.zju.edu.cn](http://one.zju.edu.cn)的场地资源申请数据 并按照黑白名单过滤 [Code](zjuactivity.py)
* 生成表格HTML [Code](zjuactivity_generate_pic.py)
* 使用wkhtmltoimage生成png图片 [Code](zjuactivity_generate_pic.py) 依赖：[imgkit](https://github.com/jarrekk/imgkit)，[wkhtmltoimage](https://wkhtmltopdf.org)
* 上传图片至upyun CDN 并清除缓存 [Code](zjuactivity_generate_pic.py) 依赖：[upyun](https://github.com/upyun/python-sdk)

### 如果你想运行

```
apt update
apt install -y git nodejs # for execjs
pushd /tmp
curl -L -o wkhtmltox.tar.xz https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
tar -xJf wkhtmltox.tar.xz
popd
git clone https://github.com/zjuchenyuan/zjuauthme
cd zjuauthme
cp /tmp/wkhtmltox/bin/wkhtmltoimage ./
pip3 install requests bs4 pyexecjs imgkit upyun

vim secret.py # write your config: zuinfo_username, zuinfo_password, and upyun.UpYun instance up
python3 zjuactivity_generate_pic.py
```