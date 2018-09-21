#windows下scrapy 安装
1.pip install wheel #python轮子，安装后就可以使用wheel文件来装软件
2.pip install lxml
3.pip install pyopenssl
4.pip install pywin32 或者 手动下载安装pywin32:https://sourceforge.net/projects/pywin32/files/pywin32/
5.手动安装twisted:wheel文件，pip安装会报错。http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
6.下载后执行pip安装twisted的wheel文件：pip install Twisted-18.7.0-cp36-cp36m-win32.whl

7.pip install scrapy



#命名行工具
一、查看帮助
scrapy -h

二、创建爬虫相关
1.全局的命令
startproject #创建项目
genspider #创建爬虫程序
settings #在项目目录下，则得到的是该项目的配置
shell #scrapy shell url地址 在交互模式下调试
fetch #独立地爬取一个页面，可以拿到请求头信息
view #下载鞍鼻直接弹出浏览器
runspider #运行一个独立的python文件
version #查看scrapy版本

2.项目中的命令
crawl #运行爬虫，必须创建爬虫项目
check #检测项目中有无语法错误
list #列出项目中的爬虫名
eidt #编辑器
parse #scrapy parse url地址 --callback 回调函数 #以此可以验证我们的回调函数是否正确
bech #scrapy bentch压力测试


