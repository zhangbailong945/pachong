##修改update
db.collection.update(
    <query>,
    <update>,
    {
        upsert:<boolean>,
        multi:<boolean>,
        writeConcern:<document>
    }
)

query:相当于where条件
update:update的对象和一些更新的操作符
upsert：可选，默认为false，代表入股都不存在update的记录不更新也不插入，设置为true代表插入。
multi：可选，默认为false,代表只更新找到的第一条记录，设置为true，代表更新所有。
writeConcern:可选，抛出异常的级别。
更新操作是不可分割的：若两个更新同时发送，先到达服务器的先执行，然后执行另外一个。

#1.覆盖式
db.users.update({'age':10},{"name":"zhangsan4"})

#2.是一种最简单的更新就是用一个新的文档完全替换匹配的文档。这种适用于大规模式的迁移。
var obj=db.users.findOne({"_id":2})
obj.username=obj.name+'SB'
obj.hobbies_count++
delete obj.age
db.users.update({"_id":2},obj)

#设置$set
#1.update db.users set name='zhangsan' where age=10
db.users.update({"age":10},{"$set":{"name":"lisi"}})

#2.如果没有匹配成功则新增一条{"upsert":true}
db.users.update({"age":10},{"$set":{"name":"zhangsan"}},{"upsert":true})

#3.修改多条
db.users.update({'age':10},{"$set":{"age":20}},{"multi":true})

#4.修改内嵌文档，把名字为zhangsan的人所在性别改为1
db.users.update({"name":"zhangsan"},{"$set":{"sex":1}},{"upsert":true},{"multi":true})

#5.把名字为zhangsan3的人的年龄改为20
db.users.update({"name":"zhangsan3"},{"$set":{"age":20}})

#6.删除zhangsan的年龄,$unset
db.users.update({"name":"zhangsan"},{"$unset":{"age":""}})


#增加或减少
#1.所有人的年龄增加一岁
db.users.update({},{"$inc":{"age":1}},{"multi":true})

#2.所有人的年龄减2岁
db.users.update({},{"$inc":{"age":-2}},{"multi":true})


#添加删除数组内的元素
#添加
db.users.update({"name":"zhangfan"},{"$push":{"hobbies":"read"}},{"upsert":true})

#为名字为zhangfan的人一次添加多个爱好game,basketball
db.users.update({"name":"zhangfan"},{"$push":{"hobbies":{"$each":["game","basketball"]}}})

#删除$pop  按照位置只能从开头或结尾删除元素
#从结尾1
db.users.update({"name":"zhangfan"},{"$pop":{"hobbies":1}})

#从开头-1
db.users.update({"name":"zhangfan"},{"$pop":{"hobbies":-1}})

#按照条件删除元素,$pull把符合条件的统统删除，而$pop只能从两端
db.users.update({"name":"zhangfan"},{"$pull":{"hobbies":"game"}},{"multi":true})

#避免添加重复
db.urls.insert({"_id":1,"urls":[]})







