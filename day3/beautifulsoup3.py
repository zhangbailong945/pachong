#搜索文档书
#五种过滤器

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

from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,'lxml')

#1.五种过滤器：字符串、正则表达式、列表，True、方法
#1.1 字符串：即标签名

print(soup.find_all('b'))

#1.2 正则表达式
import re
print(soup.find_all(re.compile('^b'))) #找出b开头的标签，结果有body和b标签


#1.3 列表
print(soup.find_all(['a','b']))

#1.4 True，可以匹配任何值，
print('======111>')
print(soup.find_all(True))
for tag in soup.find_all(True):
    print(tag.name)

#1.5 函数，如果没有合适过滤器，那么可以定义一个方法，方法只接受一个元素参数，如果这个方法返回True，
#表示当前元素匹配并被找到，如果不是则返回False
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
print('=====>1.5')
print(soup.find_all(has_class_but_no_id))