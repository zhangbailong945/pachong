import re

#re 提供了其他方法

#1 re.findall(pattern,str) #返回所有满足匹配的结果，放在列表
print(re.findall('a','loach zhangsan lisi')) #result:['a', 'a', 'a']

#2 re.search(pattern,str).group() #只要找到第一个匹配然后返回一个包含匹配信息的对象，该对象返回通过group()方法得到匹配的字符串，没有返回None
print(re.search('a','loach zhangsan lisi').group()) #result:a

#3 re.match(pattern,str) #同search，不过在字符串开始处进行匹配，可以哦难怪search+^代替
print(re.match('a','loach zhangsan lisi')) #result:None

#4 re.split(pattern,str) #分隔
print(re.split('[ab]','abcd')) #先按'a'分隔得到''和'bcd'，再对''和'bcd'分别按b分隔最后结果：['','','cd']


#5 re.sub(old,new,str,n) 在str中的old字符串替换为new字符串，替换n个，默认全部
print(re.sub('a','A','zhangsan haoa')) #result:zhAngsAn hAoA
print(re.sub('a','A','zhangsan haoa',1)) #result:zhAngsan haoa
print(re.sub('a','A','zhangsan haoa',2)) #zhAngsAn haoa

print('===>',re.sub('^(\w+)(.*?\s)(\w+)(.*?\s)(\w+)(.*?)$',r'\5\2\3\4\1','alex make love')) 
#result:===> love make alex 

#6 re.subn(old,new,str) 返回结果带有替换的个数
print(re.subn('a','A','zhangsan haoa')) #result:('zhAngsAn hAoA', 4)

#7 re.compile(pattern) 根据包含的正则表达式的字符串创建模式对象。可以实现更有效率的匹配。
obj=re.compile('\d{2}')
print(obj.search('abc123eeee').group()) #12
print(obj.findall('abc123eee')) #['12'] 重用了12

