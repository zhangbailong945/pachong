import redis

client=redis.Redis(host="localhost",port=6379,db=0)
client.flushdb()

client.zadd("age",'zhangsan',50,'lisi',25,'zhaoliu',35,'wangwu',40)


print(client.zcard('age'))

print(client.zcount('age',40,70))

print(client.zrank('age','zhangsan'))