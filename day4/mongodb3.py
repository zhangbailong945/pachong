#数据库操作

#1.增
use dbname #如果dbname数据库不存在，则创建数据库，否则为切换到dbname数据库

#2.查
#2.1查看所有数据库
show dbs 
#刚创建的空数据库，需要插入数据才能显示
use long
db.users.insert({'name':'long'})

#3.删
use long #先切换到要删的库下
db.dropDatabase() #删除当前数据库

