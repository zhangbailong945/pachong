#查询数组

#1.查询所有
db.users.find({"age":{"$gte":12}})

#2.查询所有爱好为篮球和游戏的人
db.suers.find(
    "hobbies":{
        "$all":["basketball","game"]
    }
)

#3.查询第四个爱好为game
db.users.find({"hobbies.3":"game"})

#4.查询所有人最后两个爱好
db.users.find({},{'hobbies':{"$slice":-2},"age":0,"name":0})

#5.查询所有人的第二个到第三个爱海
db.users.find({},{'hobbies':{"$slice":[1,2]},"age":0,"name":0})

#6.格式化返回的数据
db.users.find().pretty()

#7.查询最后两个
db.users.find({"$slice":-2})

#8. 查询1到2
db.users.find({},{"hobbies":{"$slice":[1,2]}}).pretty()

#####排序：1代表生效，-1代表降序
db.users.find().sort({"age":1})
db.users.find().sort({"age":-1})

#####分页：limit代码去多少个document,skip代码跳过当前多少个document
db.users.find().sort({'age':1}).limit(1).skip(2)

#####统计：
db.users.count({"age":{"$gt":10}})
#或者
db.users.find({"age":{"$gt":10}}).count()


##null
db.users.insert({"name":"lisi","age":null})
db.users.insert({"name":"wangwu"})
db.users.insert({"age":null})

##查找一条数据
db.users.findOne("age":{"$gt":10})