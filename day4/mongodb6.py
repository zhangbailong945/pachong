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

#SQL: and or not
#MongoDB:字典中逗号分隔的多个条件是and关系，$or的条件放在[]内，$not

#1.select * from db1.users where age>=10 and age <13
db.users.find({'age':{"$gte":2,"$lt":13}})

#2.select *from db.users where age>=10 and name="zhangsan"
db.users.find({'age':{"$gte":1},"name":"zhangsan"})

#3.select * from db.users where age>=12 or name='zhangsan'

db.users.find({
    "$or":[
        {'age':{"$gte":12}},
        {"name":"zhangsan"}
        ]
})

#4.select * from db1.users where age % 2=1
db.users.find({"age":{"$mod":[2,1]}})

#5. 4取反
db.users.find({"age":{"$not":{"$mod":[2,1]}}})


#成员运算

#SQL：in ,not in
#MongoDB:"$in","$nin"

#1.select * from db.users where age in(10,12,13)
db.users.find({"age":{"$in":[10,12]}})

#2.select * from db.users where name not in ("zhangsan2","zhangsan3")
db.users.find({"name":{"$nin":["zhangsan2","zhangsan3"]}})

#正则表达式
#SQL:regexp 正则
#MongoDB /正则表达式/i

#1.select * from db.users where name regexp '^z.*?(g|3)$'
db.users.find({"name":/^z.*?(g|3)$/i})

#去指定字段
#1.select name,age from db.users where name='zhangsan'
db.users.find({{"name":"zhangan"},{"_id":0,'name':1,'age':1}})



