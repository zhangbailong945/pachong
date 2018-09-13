#集合操作

#1.增
#当第一个文档插入时，集合就会被创建
use long
db.table1.insert({'name':'long'})
db.table2.insert({'name':'loach'})

#2.查
show tables

#3.删
use long
db.table1.drop()



