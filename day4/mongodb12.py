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

###投射
#用法：{"$project":{"要保留的字段名":1,"要去掉的字段名":0,"新增的字段名":"表达式"}}

#1、select name,post,(age+1) as new_age from db1.emp
db.emp.aggregate(
    {
        "$project":{
            "_id":1,
            "name":1,
            "post":1,
            "new_age":{"$add":["$age",1]}
        }
    }
)


#2.表达式之数学表达式
{"$add":[expr1,expr2,....,exprN]}  #相加
{"$subtract":[expr1,expr2]} #第一个减去第二个
{"$multiply":[expr1,expr2,...,exprN]} #相乘
{"$divide":[expr1,expr2]} #第一个表达式除以第二个表达式的商作为结果
{"$mod":[expr1,expr2]} #第一个表达式除以第二个表达式的余数作为结果


#3.表达式日期表达式
#$year,$month,$week,$dayOfMonth,$dayOfWeek,$dayOfYear,$hour,$minute,$second,
#例如：select name,date_format("%Y") as date from db1.emp
db.emp.aggregate(
    {"$project":{"name":1,"date":{"$year":"$date"}}}
)

#查询每个员工的工作多长时间
db.emp.aggregate(
    {
        "$project":{
            "name":1,"work_time":{
                "$subtract":[
                    {"$dayOfYear":new Date()},
                    {"$dayOfYear":"$date"}
                ]
            }
        }
    }
)


###字符串表达式
{"$substr":[字符串/$值为字符串的字段名，起始位置，截取几个字节]}
{"$concat":[expr1,expr2,...,exprN]} #指定的表达式或字符串连接在一起返回，只支持字符串拼接
{"$toLower":expr}
{"$toUpper":expr}

db.emp.aggregate(
    {
        "$project":{
            "name":{
                "$toUpper":"$name"
            }
        }
    }
)

#逻辑表达式
$and 
$or
$not 

