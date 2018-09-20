#改进方案：线程池或进程池+异步调用：提交一个任务后并不会等待任务结束，而是继续下一行代码
'''
很多程序员可能会考虑使用“线程池”或“连接池”.线程池旨在减少创建和销魂线程的频率，其维持一定合理数量的线程，并让控线的线程重新承担行的执行任务。
连接池维持连接的缓存池，尽量重用已有的连接、减少创建和关闭连接的频率。这两种技术都可以很好地降低系统开销，都被广泛应用很多大型系统，如：websphere、tomcat和各种数据库等。
'''

import requests,time
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def parse_page(res):
    res=res.result()
    print('%s 解析 %s'%(current_thread().getName(),len(res)))


def get_page(url):
    print("%s 下载 %s"%(current_thread().getName(),url))
    response=requests.get(url)
    if response.status_code==200:
        return response.text


if __name__=='__main__':
    urls=[
        'https://www.baidu.com',
        'https://www.sina.com.cn',
        'https://www.python.org'
    ]
    start=time.time()
    pool=ThreadPoolExecutor(50)
    for url in urls:
        pool.submit(get_page,url).add_done_callback(parse_page)
    pool.shutdown(wait=True)
    end=time.time()
    print(end-start)

##存在问题
#线程池和连接池技术也只是在一定程度上缓解了频繁调用IO接口带来的资源占用。而且，所谓池始终尤其上限，
#当请求大大超过上限时，池构成的系统对客户端的响应并不必没有池的时候效率好多少，所以池必须考虑其面临的响应规模，并根据响应规模调整池的大小。