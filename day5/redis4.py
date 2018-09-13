#string

#1.set(name,value,ex=None,px=None,nx=False,xx=False)
#在redis中设置值，默认，不存在则创建，存在则修改
#参数：
#ex,过期时间(秒)
#px,过期时间(毫秒)
#nx,如果设置为True,则只有name不存在时，当前set操作才执行
#xx，如果设置为True，则只有name存在时，当前set操作才执行

#2.setnx(name,value)
#设置值，只有name不存在时，执行设置操作


#3.setex(name,value,time)
#设置值，time过期时间（秒或timedelat对象）

#4.psetex(name,time_ms,value)
#设置值 time_ms,过期时间

#5.mset(*args,**kwargs)
#批量设置值


#6.get() 
#取值

#7.mget(keys,*args)
#批量获取值


#8.getset(name,value)
#设置新值并获取原来的值

#9.getrange(key,start,end)
#获取子序列

#10.setrange(name,offset,value)
#修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
#一个汉字3个字节

#11.strlen(name)
#返回name对应值的字节长度(一个汉字3个字节)

#12.incr(self,name,amount=1)
#自增 name="1" 对应值，当name不存在时，则创建name=amount,否则自增。


#13.incrbyfloat(self,name,amount=1.0)

#14.decr(self,name,amount=1) #自减

#15.append(key,value)
#在redis name对应的值后面追加内容



