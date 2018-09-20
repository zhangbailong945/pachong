#但asyncio模块只能发tcp级别的请求，不能发http协议，因此在发送http请求的时候，
#需要我们自定义http报头

import asyncio
import requests
import uuid

user_agent="""Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"""

#解析页面
def parse_page(host,res):
    print('%s 解析结果 %s'%(host,len(res)))
    with open('%s.html'%(uuid.uuid1()),'wb') as f:
        f.write(res)

#异步阻塞
@asyncio.coroutine
def get_page(host,port=80,url='/',callback=parse_page,ssl=False):
    print('下载 http://%s:%s%s'%(host,port,url))
    #步骤一（IO阻塞）：发起tcp链接，是阻塞操作，因此需要yield from
    if ssl:
        port=443
    recv,send=yield from asyncio.open_connection(host=host,port=443,ssl=ssl)
    #步骤二：封装http协议报头，因为asyncio模块只能封装并发送tcp包
    request_heads="""GET %s HTTP/1.0\r\nHost: %s\r\nUser-agent: %s\r\n\r\n"""%(url,host,user_agent)
    request_heads=request_heads.encode('utf-8')

    #步骤三:发送http请求包
    send.write(request_heads)
    yield from send.drain()

    #步骤四：接受响应头
    while True:
        line=yield from recv.readline()
        if line==b'\r\n':
            break;
        print('%s Response headers:%s'%(host,line))
    
    #步骤五、接受响应体
    text=yield from recv.read()

    #执行回调函数
    callback(host,text)

    #步骤七：关闭套接字
    send.close() 


if __name__=='__main__':
    tasks=[
        get_page('www.baidu.com',url='/s?wd=美女',ssl=True),
        get_page('www.cnblogs.com',url='/',ssl=True)
    ]
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    



