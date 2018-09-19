import redis

client=redis.StrictRedis(host='localhost',port=6379,db=0)
client.flushdb()
client.lpush('list1',1,2,3)
client.lpush('list2','a','b','c')
'''
print(client.blpop(["list1","list2"]))
print(client.blpop(["list1","list2"]))
print(client.blpop(["list1","list2"]))
print(client.blpop(["list1","list2"]))
print(client.blpop(["list1","list2"]))
print(client.blpop(["list1","list2"]))
print(client.blpop(["list1","list2"],timeout=3))#阻塞3秒，返回None
'''

#自定义增量迭代
def list_iter(name):
    '''
    自定义redis列表增量迭代
    param name:redis中的name,即迭代name对应的列表
    return yield 返回 列表元素
    '''
    list_count=client.llen(name)
    for index in range(list_count):
        yield client.lindex(name,index)


#使用
for item in list_iter('list1'):
    print(item)
