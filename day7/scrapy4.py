#spiders
#1.介绍
#Spiders是由一系列（定了一个网址或一组网址将被爬取）组成，具体包括如何执行爬取任务并且如何从页面提取结构化数据。
#爬什么，怎么爬

#2.Spider会循环做如下事情
#2.1 生成初始的Requests来爬取第一个urls，并标识一个回调函数
'''
第一个请求定义在start_requests()方法内默认从start_urls列表中获取url地址来生成
request请求，默认的回调函数是parse()方法。回调函数在下载完成返回response时自动触发。
'''

#2.2 在回调函数中，解析response并且返回值
#返回值有4种：
'''
包含解析数据的字典
Item对象
新的Request对象
可迭代对象
'''

#3.在回调函数中解析页面内容
#通常使用scrapy自带的Selectors,也可以使用第三方Beutifulsoup,lxml等

#4.针对返回的Item对象将会持久化到数据库
'''
通过Item Pipeline组件存到数据库
https://docs.scrapy.org/en/latest/topics/item-pipeline.html
或者导出到不同的文件
https://docs.scrapy.org/en/latest/topics/feed-exports.html
'''

#Spiders总共提供了五种类
'''
1.scrapy.spiders.Spider
2.scrapy.spiders.CrawlSpider
3.scrapy.spiders.XMLFeedSpider
4.scrapy.spiders.SCVFeedSpider
5.scrapy.spiders.SitemapSpider
'''

#牛刀小试

import scrapy 
from scrapy.spider import Spider

#自定义类，继承scrapy.spiders.Spider

class HuanYueSpider(scrapy.Spider):
    name='HuanYue'
    allowed_domains=['www.huanyue123.com']
    start_urls=['http://www.huanyue123.com/']

    def parse(self,response):
        print(response.status_code)


#爬虫程序分析
#1.name='HuanYue'
'''
定义怕重名,scrapy会根据该值定位爬虫程序,必须唯一
'''

#2.allowed_domains=['www.huanyue123.com']
'''
定义允许爬虫的域名，OffsiteMiddleware启动，默认启动
'''

#3.start_urls=['http://www.huanyue123.com/']
'''
如果没有指定url,就从该列表中读取url来生成第一个请求
'''

#4.custom_settings
'''
值为一个字典，定义一些配置信息，在爬虫程序运行是，该配置会覆盖掉项目级别的配置
'''

#5.settings
'''
通过self.settings['配置项的名字] 可以访问settings.py中的配置，除非自定义custom_settings覆盖
'''

#6.logger
'''
日志名默认为spider的名字
self.logger.debug('=====>%s'%self.settings['NAME'])

'''

#5.crawler
'''
该属性必须被定义到类方法from_crawler中
'''

#6.from_crawler(crawler,*args,**kwargs)

#7.start_requests()
'''
该方法用来发起第一个Request请求，且必须返回一个可迭代的对象，它在爬虫程序
打开时就被scrapy调用，scrapy值调用它一次
默认从start_urls里取每个来生成Request(url,dont_filter=True)
'''

#如果想要改变其实爬取的Requests，就必须覆盖这个方法。

class MySpider(scrapy.Spider):
    name='myspider'

    def start_requests(self):
        return [scrapy.FormRequest('http://huanyue123.com/',formdata={'user':'user','pass':'pass',callback=self.logined})]
    
    def logined(self,response):
        pass

#8.parse(response)
#这是默认的回调函数，所有的回调函数必须返回一个可迭代的对象

#9.log(message)

#10.closed(reason)
#爬虫结束时自动触发

