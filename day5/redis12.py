#其他操作

#1、delete(*names)
#根据name删除redis中的任意数据类型

#2.exists(name)
#检测redis的name是否存在

#3.keys(pattern='*')
#根据模型获取redis的name

#4.expire(name,time)
#为某个redis的某个name设置超时时间

#5.rename(src,dst)
#对redis的name重命名

#6.move(name,db)
#将redis的某个值移动到指定的db下

#7.randomkey()
#随机获取一个redis的name

#8.type(name)
#获取name对应的数据类型

#9.scan(cursor=0,match=None,count=None)
#10.scan_iter(match=None,count=None)
#同字符串操作，用于增量迭代获取key

