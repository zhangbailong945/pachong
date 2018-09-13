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

#6.