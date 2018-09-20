#twisted 是一个网络框架，其中一个功能是发送异步请求，检测IO并自动切换

#twisted 基本用法

from twisted.web.client import getPage,defer
from twisted.internet.reactor import sto

def all_done(arg):
    reactor.stop()

def callback(res):
    print(res)
    return 1

defer_list=[]
urls=[
    'https://www.baidu.com',
    'https://www.sina.com.cn',
    'https://www.python.org',
]

for url in urls:
    obj=getPage(url.encode('utf=-8'),)
    obj.addCallback(callback)
    defer_list.append(obj)

defer.DeferredList(defer_list).addBoth(all_done)
reactor.run()