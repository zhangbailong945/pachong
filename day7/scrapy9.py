#下载中间件的用途
#1.在process-resquest，自定义下载，不用scrapy的下载
#2.对请求进行二次加工，比如,设置请求头，设置cookie，添加代理
#scrapy自带的代理组件
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from urllib.request import getproxies


