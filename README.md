# zjuauthme & zjuactivity
Login ZJU Unified Identity Authentication system using Python3

## ZJU Activity

* 登录统一通行证 [Code](zjuauthme.py) 依赖：[execjs](https://pypi.python.org/pypi/PyExecJS) [EasyLogin](https://github.com/zjuchenyuan/EasyLogin)
* 爬取[http://one.zju.edu.cn](http://one.zju.edu.cn)的场地资源申请数据 并按照黑白名单过滤 [Code](zjuactivity.py)
* 生成表格HTML [Code](zjuactivity_generate_pic.py)
* 使用wkhtmltoimage生成png图片 [Code](zjuactivity_generate_pic.py) 依赖：[imgkit](https://github.com/jarrekk/imgkit)，[wkhtmltoimage](https://wkhtmltopdf.org)
* 上传图片至upyun CDN 并清除缓存 [Code](zjuactivity_generate_pic.py) 依赖：[upyun](https://github.com/upyun/python-sdk)

## 执行结果

[今天有哪些活动？](https://api.py3.io/zjuactivity_today.png)

[明天有哪些活动？](https://api.py3.io/zjuactivity_tomorrow.png)

## 如果你想运行

以下命令基于Ubuntu 16.04容器，执行的操作有：
* 修复容器的locale和时区设置，以免容器默认POSIX无法输出中文
* 安装微软雅黑字体，请从windows机器中自行复制
* apt-get、pip安装上述提到的所有依赖，其中nodejs是为了python执行js而安装的
* 配置secret.py
* 执行咯~

```
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
echo "nameserver 10.10.0.21"> /etc/resolv.conf

# You need to copy msyh.ttc from a Windows computer, C:\Windows\Fonts\msyh.ttc, I cannot supply it here
cp msyh.ttc /usr/share/fonts/

apt update
apt install -y git nodejs libfontconfig1 libxrender1 curl python3-pip

pip3 install requests bs4 pyexecjs imgkit upyun -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com

pushd /tmp
curl -L -o wkhtmltox.tar.xz https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
tar -xJf wkhtmltox.tar.xz
popd

git clone https://github.com/zjuchenyuan/zjuauthme
cd zjuauthme
cp /tmp/wkhtmltox/bin/wkhtmltoimage ./

vim secret.py # write your config: zuinfo_username, zuinfo_password, and upyun.UpYun instance up
python3 zjuactivity_generate_pic.py
```

在按上述命令准备好docker容器后，可以制作为镜像，镜像名称zjuactivity，以后就能这么运行了：（也就是环境变量、DNS、工作目录要记得设置）

```
docker run --rm --dns 10.10.0.21 -w /zjuauthme -e LC_ALL=C.UTF-8 -e LANG=C.UTF-8 zjuactivity python3 zjuactivity_generate_pic.py
```

#### secret.py

这是一个secret.py的例子，按需替换为你的值：

```
import upyun
up = upyun.UpYun('服务名称' ,username='操作员用户名',password='操作员密码') # 注意操作员应该对 服务名称 这个CDN服务有完全权限
zuinfo_username = "学号"
zuinfo_password = "统一通行证密码"
```

## 欢迎贡献

发现了bug? 有建议? 欢迎提Issue~

都看到这里了，来给我个Star吧 =￣ω￣=