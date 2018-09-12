#遍历文档树

html_doc="""
<html>
<head>
<title>title name</title>
</head>
<body>
<p id="my p" class="title"><b id="bbb" class="boldset">I'm title</b></p>
<p class="content">content there is </p>
<a href="https://www.baidu.com">百度</a>
<a href="https://www.baidu.com">百度</a>
<a href="https://www.baidu.com">百度</a>
<p class="detail">
详情内容
</p>
</body>
</html>
"""

#1.使用
from bs4 import BeautifulSoup

soup=BeautifulSoup(html_doc,'lxml')

#2.获取标签及其内容，有多个只返回第一个
print(soup.p)
print(soup.a)

#3.获取标签的名称
print(soup.p.name)

#4.获取标签的属性
print(soup.p.attrs)

#5.获取标签的内容
print(soup.p.string) #只有一个文本，返回文本，否则为None
print(soup.p.strings) #难当一个生成器对象，取到p下所有的文本内容
print(soup.p.text) #取到p下所有的文本内容

for line in soup.stripped_strings: #去掉空白
    print(line)


#6.嵌套选择
print(soup.head.title.string)
print(soup.body.a.string)

#7.子节点，子孙节点
print(soup.p.contents) #p下所有子节点
print(soup.p.children) #得到一个迭代器，包含p下所有的子节点

for i,child in enumerate(soup.p.children):
    print(i,child)


print(soup.p.descendants) #获取子孙节点，p下所有的标签都会选择出来

for i,child in enumerate(soup.p.descendants):
    print(i,child)


#8、父节点、祖先节点
print(soup.a.parent) #获取a标签的父节点
print(soup.a.parents) #获取a标签所有的祖节点

#9.兄弟节点
print('=====>')
print(soup.a.next_sibling) #下一个兄弟
print(soup.a.previous_sibling) #上一个兄弟

print(list(soup.a.next_siblings)) #下面的兄弟们=》生成器对象
print(soup.a.previous_siblings) #上面的兄弟们=》生成器对象

