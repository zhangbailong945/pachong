import scrapy


class MyScrapy(scrapy.Spider):
    name='scrapy5'
    allowed_domains=['example.com']
    start_urls=[
        'http://www.example.com/1.html',
        'http://www.example.com/2.html',
        'http://www.example.com/3.html',
    ]

    def parse(self,response):
        self.logger.info('A respoonse from %s juse arrived!',response.url)
    
    