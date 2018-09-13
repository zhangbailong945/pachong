#比较运算符

#SQL:=,!=,>,<,>=,<=
#MongoDB：{key:value} 代表key等于value,$ne,$ge,$lt,$gte,$lte,

#1.selct * from db.users where name='zhangsan'
db.users.find({'name':'zhangsan'})

#2.select * from db.users where name!='zhangsan'
db.users.find({'name':{'$ne':'zhangsan'}})

#3.select * from db.users where age>2
db.users.find({'age':{'$gt':12}})

#4.select * from db.users where age<13
db.users.find({'age':{'$lt':13}})

#5.select * from db.users where age>=10
db.users.find({'age':{'$gte':10}})

#6.select * from db.users where age<=12
db.users.find({'age':{'$lte':12}})


#逻辑运算