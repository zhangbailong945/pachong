#MongoDB 是一个基于分布式文件存储的数据库

"""
它的特点是高性能、易部署、易使用，存储数据非常方便。主要功能特性有：
*面向集合存储，易存储对象类型的数据。
mongodb集群参考
mongodb集群参考
*模式自由。
*支持动态查询。
*支持完全索引，包含内部对象。
*支持查询。
*支持复制和故障恢复。
*使用高效的二进制数据存储，包括大型对象（如视频等）。
*自动处理碎片，以支持云计算层次的扩展性。
*支持RUBY，PYTHON，JAVA，C++，PHP，C#等多种语言。
*文件存储格式为BSON（一种JSON的扩展）。
*可通过网络访问
"""

#安装：https://www.mongodb.com/download-center?jmp=nav#community

#1.下载后，单击exe程序，选择自定义目录，取消勾选安装compass工具，并手动输入数据库目录和日志目录
#例子：安装路径问D:/MongoDB,可以将D:/MongoDB/Server/4.0/bin 加入 我的电脑=》属性=》高级设置=》坏境变量=》系统变量=》path中去

#2.新建数据目录和日志文件
#例子：D:/MongoDB/data/db  D:/MongoDB/log/mongod.log

#3.自定义配置文件mongod.cfg
#可以参考官网：https://docs.mongodb.com/manual/reference/configuration-options/#configuration-file

'''
systemLog:
   destination: file
   path: "D:/MongoDB/log/mongod.log"
   logAppend: true
storage:
   journal:
      enabled: true
   dbPath: "D:/MongoDB/data/db"
processManagement:
   fork: true
net:
   bindIp: 127.0.0.1
   port: 27017
setParameter:
   enableLocalhostAuthBypass: false
'''

#4.生成系统服务
#单击D:/MongoDB/Server/4.0/bin/mongo.exe,弹出命令行输入一下命令：
mongod --config "D:/MongoDB/mongod.cfg" --bind_i 0.0.0.0 --install
#或者命令行输入 win+r cmd mongo ，输入一下命令
mongod --bind_ip 0.0.0.0 --port 27017 --logpath d:/mongodb/log/mongod.log --logappend --dbpath d:/mongodb/data/db --serviceName "MongoDb" --serviceDiplayName "MongoDB" --install




