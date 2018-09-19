#sort set 有序序列集合

#1.zadd(name,*args,**kwargs)
#在name对应的有序集合中添加元素

#2.zcard(name)
#获取name对应的有序集合中元素的个数

#3.zcount(name,min,max)
#获取name对应的有序集合中年龄在[min,max]之间的个数


#4.zincrby(name,value,amount)
#自增name对应的有序集合的name对应的年龄

#5.zrange(name,start,end,desc=False,withscores=False,score_cast_func=float)
#按照索引范围获取name对应的有序集合的元素
#从大到小排序
#zrevrange(name,start,end,withscores=False,score_cast_func=float)
zrangebyscore(name,min,max,start=None,num=None,withscores=False,score_cast_func=float)
zrevrangebyscore(name,min,max,start=None,num=None,withscores=False,score_cast_func=float)

#6.zrank(name,value)
#获取某个值在name对应的有序集合中的排行
#从大到小 zrevrank(name,value)

#7.zrangebylex(name,min,max,start=None,num=None)
#当有序集合的所有成员具有相同的分值时，
#从大到小 zrevrangebylex(name,max,min,start=None,num=None)

#8.zrem(name,values)
#删除name对应的有序集合中值是values的成员

#9.zremrangebyrank(name,min,max)
#根据排序范围删除

#10.zremrangebysocre(name,min,max)
#根据分数范围删除

#11.zremrangebylex(name,min,max)
#根据值返回删除

#12.zscore(name,value)
#获取name对应有序集合中value对应的分数

#13.zinterstore(dest,keys,aggregate=None)
#获取两个有序集合的交集，如果遇到相同值不同分数，则按照aggregate进行操作：SUM,MIN,MAX

#14.zunionstore(dest,keys,aggregate=None)
#获取两个有序集合的并集，如果遇到相同值不同分数，则按照aggregate进行操作

#15.zscan(name,cursor=0,match=None,count=None,score_cast_func=float)
#16.zsan_iter(name,match=None,count=None,score_cast_func=float)




