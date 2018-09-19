#list

#1.lpush(name,values)
在name对应的list中添加元素，每个新的元素都添加到列表的最左边
rpush(name,values)


#2.lpushx(name,value)
在name对应的list中添加元素，只有name存在时，值添加到列表的最左边
rpushx(name,value)

#3.llen(name)
name对应的list元素的个数

#4.linsert(name,where,refvalue,value)
在name对应的列表的某一个值前或后插入一个新值

#5.r.lset(name,index,value)
在name对应的list中的某一个索引位置重新赋值

#6.r.lrem(name,value,num)
在name对应的list中删除指定的值
参数：
name,redis的name
value 要删除的值
num,num=0，删除列表中所有指定的值,num=2，从前到后删除2个，num=-2，从后往前删除2个

#7.r.lpop(name)
在name对应的列表中的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
r.rpop(name) 表示从右向左操作

#8.r.lindex(name)
在name对应的列表中根据索引获取列表元素

#9.lrange(name,start,end)
在name对应的列表中分片获取数据

#10.r.ltrim(name,start,end)
在name对应的列表中移除没有在start-end索引之间的值

#11.r.rpoplpush(src,dst)
从一个列表取出最右边的元素，同时将其添加到另一个列表的最左边
src，要取数据的列表的name
dst,要添加数据的列表的name

#12.blpop(keys,timeout)
keys={"k1","k2"} #按照从左到右去pop对应列表的元素


#13.r.brpoplpush(src,dst,timeout=0)
从一个列表的右侧移除一个元素并将其添加到另一个列表的左侧

#14.自定义迭代
由于redis类库中没有提供对应列表元素的增量迭代，如果要循环name的对应的列表的所有元素。那么就需要
1.获取name对应的所有列表
2.循环列表
如果太大，会撑爆内存。

