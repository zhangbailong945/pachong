import redis


client=redis.StrictRedis(host="localhost",port=6379,db=0)
client.flushdb()

#1.向集合中添加元素
client.sadd('set1',1,2,3,4,4,5)

#1.统计Set中元素的个数
print(client.scard('set1'))

print(client.smembers('set1'))

print(client.srandmember('set1',2))

