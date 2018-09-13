#基本数据类型

#1.null 用于表示空或者不存在的字段
d={'x':null}

#2.布尔型:true和false
d={'x':true,'y':false}

#3.数值
d={'x':3,'y':3.1415926}

#4.字符串
d={'x':'loach'}

#5.日期
d={'x':new Date()}
d.x.getHours()

#6.正则表达式
d={'pattern':/^loach&/i}  #i忽略大小写，m多行匹配，x忽略转移字符，s当行匹配模式

#7.数值
d={'x':[1,'a','loach']}

#8.内嵌文档
user={'name':'long','hobby':{'game':'lol','play':'game'}}

#9.对象id：是一个12字节的id,是文档的唯一表示，不可变
d={'x':ObjectId}



