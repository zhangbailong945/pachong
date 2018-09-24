##去重规则,爬过得url不重复爬取

#方法一
visited=set() #类属性

def parse(self,response):
    from hashlib import md5
    url=md5(response.request.url)
    if response.url in self.visited:
        return None
    

    self.visited.add(url)


#方法二：scrapy自带去重功能
配置文件:
DUPEFILTER_CLASS='scrapy.duperfilter.RFPDupeFilter' #默认去重规则，在内存存中
DUPEFILTER_DEBUG=False
JOBDIR='/root/user/scrapy/dupefilter/request.url.log'





