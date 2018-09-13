#选择数据库
import redis

pool=redis.ConnectionPool(host='localhost',port=6379,max_connections=100)
client=redis.Redis(connection_pool=pool)

client.execute_command('select 1') #数据库
