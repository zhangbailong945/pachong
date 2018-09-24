#selectors 选择器

#1.//与/
#2.text
#3.extract与extract_first: 从selector对象中解出内容
#4.属性：xpath的属性加前缀@
#5.嵌套查找
#6.设置默认值
#7.按照属性值查找
#8.按照属性模糊查找
#9.正则表达式
#10.xpath相对路径
#11.带变量的xpath

#1.1 //与/
#开头的//代表从整篇文档中寻找，body之后的/代表body的儿子
response.xpath('//body/a/') 
response.css('a')
#开头的//代表从整篇文档中寻找，body之后的//代表body的子子孙孙
response.xpath('//body//a')

#2.1 text
response.xpath('//body//a/text()')
response.css('body a::text')

#3.1 extract与extract_first
response.xpath('//body//a/text()').extract()
response.css('body a::text').extract()

response.xpath('//body//a/text()').extract_first()
response.css('body a::text').extract_first()


#4.1 属性：xpath属性加前缀@,css用attr(属性名)
response.xpath('//div/a/@href').extract_first()
response.css('div a::attr(href)').extract_first()

#5.1 嵌套查找(css和xpath交叉使用)
response.xpath('//div[@id="s_fm"]').css('a').xpath('@href').extract_first()

#6.1 设置默认值
response.xpath('//div[@id="xxx"]').extract_first(default='not found')

#7.1 按照属性查找
response.xpath('//div[@id="s_fm"]//a[@href="/"]').extract_first()




