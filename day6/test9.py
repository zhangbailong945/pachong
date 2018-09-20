#用gevent封装的requests

import grequests

request_list=[
    grequests.get('https://www.pythonxxx.org/doc'),
    grequests.get('https://www.cnblogs.com/linhaifeng'),
    grequests.get('https://www.openstack.org'),
]

###执行并获取响应列表
#response_list=grequests.map(request_list)
#print(response_list)

##执行并获取响应列表带处理异常
def exception_handler(request,exception):
    print('%s request fiald!'%request.url)

response_list=grequests.map(request_list,exception_handler=exception_handler)
print(response_list)