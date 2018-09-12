import re

#正则匹配
#\w 匹配字母、数字、下划线
#\W 匹配非字母、数字、下划线

pattern='\w'
str='loach blog 945 __'
print(re.findall(pattern,str))
#result:['l', 'o', 'a', 'c', 'h', 'b', 'l', 'o', 'g', '9', '4', '5', '_', '_']

pattern='\W'
print(re.findall(pattern,str))
#result:[' ', ' ', ' ']

#\s 匹配任意空白字符串，等价于[\t\n\r\f]
#\S 匹配任意非空字符串

pattern='\s'
print(re.findall(pattern,str))
#result:[' ', ' ', ' ']

pattern='\S'
print(re.findall(pattern,str))
#result:['l', 'o', 'a', 'c', 'h', 'b', 'l', 'o', 'g', '9', '4', '5', '_', '_']

#\r \t 都是空，都可以被\s 匹配到
pattern='\s'
str='loach \tblog \n945'
print(re.findall(pattern,str))
#result:[' ', '\t', ' ', '\n']

#\n \t
pattern1=r'\t'
pattern2=r'\n'
str1='loach\tblog\t945'
str2='loach\nblog\n945'
print(re.findall(pattern1,str1))
#result:['\t', '\t']

print(re.findall(pattern2,str2))
#result:['\n', '\n']

#\d 匹配数字
#\D 匹配非数字
pattern1='\d'
pattern2='\D'
print(re.findall(pattern1,str))
#result:['9', '4', '5']
print(re.findall(pattern2,str))
#result:['l', 'o', 'a', 'c', 'h', ' ', '\t', 'b', 'l', 'o', 'g', ' ', '\n']

#\A 匹配字符串开始,等价于^
#\Z 匹配字符串结尾,等价于$(可以匹配换行之后的),如果存在换行，则只匹配换行之前的字符串

pattern1='\Aloach'
pattern2='\Z945'
str1='loach \nblog\t945'
print(re.findall(pattern1,str1))
#result:['loach']
print(re.findall(pattern2,str1))
#result:[]

pattern1='^loach'
pattern2='945$'
print(re.findall(pattern1,str1))
#result:['loach']
print(re.findall(pattern2,str1))
#result:[945]


#. 匹配任意单个字符（除了\r\n）
pattern='a.b'
str1='a2b'
str2='assssb'
str3='ab'
print(re.findall(pattern,str1))
#result:a2b
print(re.findall(pattern,str2))
#result:[]
print(re.findall(pattern,str3))
#result:[]

#* 匹配前面子表达式0次或者多次
pattern='ab*'
str1='bbbbbbb'
str2='a'
str3='abbbbbb'
print(re.findall(pattern,str1))
#result:[]
print(re.findall(pattern,str2))
#result:[a]
print(re.findall(pattern,str3))
#result:[abbbbbb]

#匹配子表达式0次或者1次
print(re.findall('ab?','a'))
#result:a
print(re.findall('ab?','abbbbb'))
#result:ab
#匹配包含有小数点的数字
pattern='\d+\.?\d*'
str='ada12fsfas35.23fsfab1'
print(re.findall(pattern,str))
#result:['12', '35.23', '1']

#.* 默认为贪婪模式，就是只要后面的能满足正则表达式，就一直匹配下去
pattern='a.*b'
print(re.findall(pattern,'asssbssssfbab'))
#result:['asssbssssfbab']
#非贪婪模式
pattern='a.*?b'
print(re.findall(pattern,'asssbssssfbb'))
#result:['asssb']


#+ 匹配子表达式1次货多次
print(re.findall('ab+','a'))
#result:[]
print(re.findall('ab+','abbb'))
#result:['abbb']


#{n,n} n,m为非负整数，n<=m,至少匹配n次，至多匹配m次
print(re.findall('ab{2}','abbb')) #result:['abb']
print(re.findall('ab{2,4}','abbbbbb'))#result:['abbbb']
print(re.findall('ab{1,}','abbb'))#result:['abbb']
print(re.findall('ab{0,}','abbb'))#result:['abbb']

#[] []内的都为普通字符，切如果没有被转移的话，应该放到[]的开头或结尾

print(re.findall('a[1*-]b','a1b a*b a-b')) #['a1b', 'a*b', 'a-b']
print(re.findall('a[^1*-]b','a1b a*b a-b a=b')) #['a=b']
print(re.findall('a[a-z]b','a1b a*b a-b acb adb'))#['acb' 'adb']
print(re.findall('a[a-zA-Z\d]b','a1b a*b a-b acb aFb aFB'))#['a1b' 'acb' 'aFb']

#rawstring 原生字符串 r'\c'
#print(re.findall('a\c','a\c')) #报错，因为\c是转义字符串
print(re.findall(r'a\\c','a\c')) #将\c当成普通字符串，原样输出

#():分组
print(re.findall('ab+','ababab123')) #result：['ab', 'ab', 'ab']
print(re.findall('(ab)+123','ababab123'))#result:['ab'] 匹配到末尾的ab123中的ab
print(re.findall('(?:ab)+123','ababab123'))#result:[ababab123] ?:可以让结果为匹配的全部内容
print(re.findall('href="(.*?)"','<a href="https://www.baidu.com">百度</a>'))#result:['https://www.baidu.com']

#x|y 匹配x或者匹配y
print(re.findall('zha(?:ng|f)','zhang san lisi zhaf jiang')) #result:['zhang', 'zhaf']
