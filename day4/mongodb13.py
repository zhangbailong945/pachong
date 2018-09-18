#分组
#用法:{"$group":{"_id":分组字段,"行的字段名称":聚合操作符}}

#1.1 分组
db.emp.aggregate({"$group":{"_id":"$sex"}}) #性别分组
db.emp.aggregate({"$group":{"_id":"$post"}}) #职位分组
db.emp.aggregate({"$group":{"_id":{"state":"$state","city":"$city"}}}) #多个字段分组

#2.1 分组后聚合得到结果，类似SQL中的：$sum,$avg,$max,$min,$first,$last
#select post,max(salary) from db1.emp group by post
#每个部门最高工资
db.emp.aggregate(
    {
        "$group":{
            "_id":"$post",
            "max_salary":{
                "$max":"$salary"
            }
        }
    }
)

#求每个部门最高工资和最低工资
db.emp.aggregate(
    {
        "$group":{
            "_id":"$post",
            "max_salary":{
                "$max":"$salary"
            },
            "min_salary":{
                "$min":"$salary"
            }
        }
    }
)

#例3：如果字段是排序后的，那么$first,$last会很有用,比$max和min效率高

db.temp.aggregate({"$group":{"_id":"$post","first_id":{"$first":"$_id"}}})

#例4：求每个部门的总工资
db.emp.aggregate({"$group":{"_id":"$post","count":{"$sum":"$salary"}}})

#例5：求每个部门的人数
db.emp.aggregate({"$group":{"_id":"$post","count":{"$sum":1}}})

#数组操作符
{"$addToSet":expr} #不重复
{"$push":expr} #重复

#例：查询岗位名以及各岗位内的员工姓名
select post,group_concat(name) from db1.emp group by post
db.emp.aggregate({"$group":{"_id":"$post","names":{"$push":"$name"}}})
db.emp.aggregate({"$group":{"_id":"$post","names":{"$addToSet":"$name"}}})
