#排序：$sort限制：$limit 跳过:$skip

{"$sort":{"字段名":1,"字段名":-1}} #1升序、-1降序
{"$limit":n}
{"$skip":n} #跳过多少个文档

#例1：取平均工资最高的前两个部门
db.emp.aggregate(
    {
    "$group":{
        "_id":"$post",
        "pingjun":{
            "$avg":"$salary"
        }
    }},
    {
        "$sort":{
            "pingjun":-1
        }
    },
    {
        "$limit":2
    }
)


##从emp中随机取3个文档
db.emp.aggregate(
    [{$sample:{size:3}}]
)