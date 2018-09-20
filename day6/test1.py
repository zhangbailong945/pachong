#同步
#1.同步调用：即提交一个任务后就原地等待任务结束，等拿到任务的结果在往后继续执行，效果地下

import requests,time

def parse_page(res):
    print('解析：%s'%(len(res)))

def get_page(url):
    print('下载%s'%url)
    response=requests.get(url)
    if response.status_code==200:
        return response.text

urls=[
    'https://www.baidu.com',
    'https://www.sina.com.cn',
    'https://www.python.org',
]

start=time.time()
for url in urls:
    res=get_page(url)
    parse_page(res)
end=time.time()
print(end-start)