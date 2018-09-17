from pymongo import MongoClient
import datetime

client=MongoClient('mongodb://root:root@localhost:27017')
table=client['db1']['emp']

l=[
    ('zhangsan','male',25,'20180917','哈哈哈哈',1000.23,401,1),#教学部
    ('lifang','male',75,'20180913','teacher',2000.23,401,1),
    ('zhangfan','female',85,'20180717','teacher',1600.23,401,1),
    ('lisi','male',55,'20180417','teacher',4000.23,401,1),
    ('zhaoliu','male',45,'20180317','teacher',4000.23,401,1),
    ('zhangxiaohong','female',19,'20180517','teacher',6000.23,401,1),
    ('wangqi','male',45,'20180717','teacher',7200.23,402,1),#以下是销售部门
    ('wangqin','female',44,'20180617','sale',5800.23,402,1),
    ('wanqing','female',47,'20180517','sale',4070.23,402,1),
    ('wanqin','male',48,'20180817','sale',3040.23,402,1),
    ('wanqi','male',78,'20180817','sale',8030.23,402,1),
    ('direnjie','male',54,'20180417','sale',9000.23,401,1),
    ('wuzetian','female',55,'20180417','developer',7000.23,402,1),#以下是开发部
    ('liyuanfang','male',65,'20180617','developer',7000.23,401,1),
    ('diruyan','female',42,'20180817','developer',7000.23,403,1),
    ('dichun','female',63,'20180617','developer',7000.23,403,1),
    ('zengtai','male',56,'20180517','developer',7000.23,403,1),
    ('hujinghui','male',33,'20180217','developer',7000.23,403,1),
    ('xueling','male',46,'20180117','developer',7000.23,403,1),
]

for n,item in enumerate(l):
    d={
        "_id":n,
        'name':item[0],
        'sex':item[1],
        'age':item[2],
        'date':datetime.datetime.strptime(item[3],'%Y%m%d'),
        'post':item[4],
        'salary':item[5]
    }
    table.save(d)

