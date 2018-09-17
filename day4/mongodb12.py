{"$match":{"字段":"条件"}},可以使用任何常用查询操作符$gt,$lt,$in等

#例子1：select * from db1.emp where post='teacher'
db.emp.aggregate({"$match":{"post":"teacher"}})


#例子2
#select * from db1.emp where id>3 group by post
db.emp.aggregate(
    {'$match':{"_id":{"$gt":3}}},
    {"$group":{"_id":"$post","avg_salary":{"$avg":"$salary"}}}
)

#例子3
#select * from db1.emp where id>3 groupby post having avg(salary)>10000a;
db.emp.aggregate(
    {"$match":{"_id":{"$gt":3}}},
    {"$group":{"_id":"$post","avg_salary":{"$avg":"$salary"}}},
    {"$match":{"avg_salary":{"$gt":6000}}}
)
