#Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.
#它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.
#Beautiful Soup会帮你节省数小时甚至数天的工作时间.
#你可能在寻找 Beautiful Soup3 的文档,Beautiful Soup 3 
#目前已经停止开发,官网推荐在现在的项目中使用Beautiful Soup 4, 移植到BS4

#安装 beautiful soup4:pip install bs4
#安装 lxml,具有容错功能

#使用
from bs4 import BeautifulSoup


html_doc="""
<html>
<head>
<title>这是测试</title>
</head>
<body>
<p class="title">BS4使用</p>
<p class="content">BS4是什么什么什么</p>
<a href="https://www.baidu.com">百度</a>
<a href="https://www.baidu.com">百度</a>
<a href="https://www.baidu.com">百度</a>
</body>
"""

soup=BeautifulSoup(html_doc,'lxml')
res=soup.prettify() #处理好缩进，结构化显示
print(res)