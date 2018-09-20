#一个简单的解决方案：多线程或多进程

#在服务器端使用多线程（或多进程），多线程和多进程的目录是让每个连接都拥有独立的线程或进程，这样任何一个连接的阻塞都不会影响其他的连接

import requests,time

from threading import Thread,current_thread

def parse_page(res):
    print("%s 下载 %s"%(current_thread().getName(),len(res)))

def get_pge(url,callback=parse_page):
    print("%s 下载 %s"%(current_thread().getName(),url))
    response=requests.get(url)
    if response.status_code==200:
        callback(response.text)


if __name__=="__main__":
    urls=[
        'https://www.baidu.com',
        'https://www.sina.com.cn',
        'https://www.python.org'
    ]
    start=time.time()
    for url in urls:
        t=Thread(target=get_pge,args=(url,))
        t.start()
    end=time.time()
    print(end-start)
#开启多进程或多线程，我们是无法限制地开启多进程或多线程：在遇到同时响应成百上千的连接请求，则无论多线程还是多进程
#都会严重占据系统资源，降低系统对客户端的响应效率，而且线程和进程本身也容易进入假死状态


