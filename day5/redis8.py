#set操作，Set集合就是不允许重复的列表

#1.sadd(name,values)
name对应的集合中添加元素


#2.scard(name)
#获取name对应的集合中的元素的个数


#3.sdiff(keys,*args)
在第一个name对应的集合中且不再其他name对应的集合的元素集合

#4.sdiffstore(dest,keys,*args)
获取第一个name对应的集合中且不再其他name对应的集合,再将其新加入到dest对应的集合中

#5.sinter(keys,*args)
获取多一个name对应集合的并集

#6.sinterstore(dest,keys,*args)
#获取多一个name对应的集合的并集，在将其加入到dest对应的集合中

#7.sismember(name,value)
#检查value是否是name对应的集合的成员


#8.smembers(name)
#获取name对应的集合的所有成员


#9.smove(src,dst,value)
#将某个成员从一个集合中移动到另外一个集合

#10.spop(name)
#从集合的右侧（尾部）移除一个成员，并将其返回

#11.srandmember(name,numbers)
#从name集合中随机获取numbers个元素

#12.srem(name,values)
#在name对应的集合中删除某些值

#13.sunion(keys,*args)
#获取多一个name对应的集合的并集


#14.sunionstore(dest,keys,*args)
#获取多一个name对应的集合的并集，并将结果保存到dest对应的集合中

#15.sscan(name,cursor=0,match=None,count=None)
#16.sscan_iter(name,match=None,count=None)
#同字符串的操作，用于增量迭代分批获取元素，避免内存消耗过大




