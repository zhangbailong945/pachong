#hash操作

#1.hset(name,key,value)
name对应的hash中设置一个键值对（不存在，则创建；否则，修改）

#2.hmset(name,mapping)
在name对应的hash中批量设置键值对


#3.hget(name,key)
在name都有的hash中根据key获取value

#4.hmget(name,keys,*args)
#在name对应的hash中获取多个key的值

#5.hgetall(name)
获取name对应hash的所有键值

#6.hlen(name)
获取name对应的hash中键值队的个数

#7.hkeys(name)
获取name对应的hash中所有的key的值

#8.hvals(name)
获取name对应的hash中所有的vaue值

#9.hexists(name,key)
检查name对应的hash是否存在当前传入的key


#10.hdel(name,*keys)
将name对应的hash中指定key的键值对删除

#11.hincrby(name,key,amount=1)
自增name对应的hash的指定key的值，不存在则创建

#12.hincrbyfloat(name,key,amount=1.0)

#13.hscan(name,cursor=0,match=None,count=None)
增量式迭代获取，对于数据大的数据非常有用,hscan可以实现分片的获取数据，并非一次将数据全部获取完，从而防止内存撑爆

参数：
    name，redis的name
    cursor，游标（基于游标分批取获取数据）
    match，匹配指定key，默认None 表示所有的key
    count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数
 
如：
    第一次：cursor1, data1 = r.hscan('xx', cursor=0, match=None, count=None)
    第二次：cursor2, data1 = r.hscan('xx', cursor=cursor1, match=None, count=None)
    ...
    直到返回值cursor的值为0时，表示数据已经通过分片获取完毕


#14.hscan_iter(name,match=None,count=None)
利用yield封装hscan创建生成器，实现分批去redis获取数据

#15.scan(match=None,count=None)
一点一点查出当前库的所有keys
