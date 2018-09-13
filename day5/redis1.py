#memcached & redis是什麼
#NoSQL數據庫，数据存到内存，读取速度快

#应用场景：页面换成
#1.简述数据库压力，提升访问速度
#2.在数据库挂掉的情况下，人能保证业务正常运行一段时间，提升安全性


#------------memcached和redis的区别
#memcached:类型单一，只能存储字符串键值对
#redis:支持五大类型数据
#1.string（字符串）
#2.list（链表）
#3.set（集合）
#4.zset（sorted set --有序集合）
#5.hash（哈希类型）

#memcached：断电数据丢失
#redis:支持持久化，单独开一个进程完成持久化，要保持性能就需要关闭持久化

#安装 https://github.com/MicrosoftArchive/redis/releases

#命令行操作：
redis-cli 
redis-cli -h host -p port -a password

#基本操作
#默认有16个数据库，编号从0-15
select 1 #切换数据

#查看所有的key
keys *

#查看所有n开头的key
keys n*

#清空redis
flushdb 

#添加key=value
set key value

#随机取一个key
randomkey

#查看key的类型
type key




