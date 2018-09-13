import redis
#连接
client=redis.StrictRedis(host='127.0.0.1',port=6379,db=0)
client.set('name','long')
v=client.get('name')

print(v,type(v))