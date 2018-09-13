#文档操作
#增

#1.没有指定_id则默认的ObjectId,_id不能重复，切在插入后不可变

#2.插入单条

user1={
    'name':'zhangsan',
    'age':10
}

db.users.insert(user1)

#3.批量插入
user2={
    'name':'zhangsan2',
    'age':12
}

user3={
    'name':'zhangsan3',
    'age':13
}

db.users.insertMany([user2,user3])




