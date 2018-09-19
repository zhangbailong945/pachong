#默认情况执行一个操作就向服务端提交一次
#可以将一系列操作放在一个管道内，一次性提交给服务端
#transaction=True,代表多个操作构成一个事务

import redis

pool=redis.ConnectionPool(host='localhost',port=6379,max_connections=100)
client=redis.Redis(connection_pool=pool)

pipe=client.pipeline(transaction=True)
pipe.set('set2','zhangsan')
pipe.set('set2','lisi')
pipe.set('set2','wangwu')

pipe.execute()