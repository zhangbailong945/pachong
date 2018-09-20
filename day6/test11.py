from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import ioloop

count=0

def handle_response(response):
    if response.error:
        print("error:",response.error)
    else:
        print(response.body)
    
    global count
    count-=1 #完成一次回调，技术减一
    if count==0:
        ioloop.IOLoop.current().stop()

def func():
    url_list=[
        'https://www.baidu.com',
        'https://www.sina.com.cn',
    ]
    global count
    for url in url_list:
        print(url)
        http_client=AsyncHTTPClient()
        http_client.fetch(HTTPRequest(url),handle_response)
        count+=1


ioloop.IOLoop.current().add_callback(func)
ioloop.IOLoop.current().start()