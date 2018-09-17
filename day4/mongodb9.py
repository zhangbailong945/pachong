#删除
#1.删除多个中的第一个
db.users.deleteOne({'age':20})

#删除多个
db.users.deleteMany({"name":zhangsan})

#删除全部
db.users.deleteMany({})