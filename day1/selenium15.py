import time,sys

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

def spider(url,keyword):
    chrome_options=Options()
    chrome_options.add_argument('--headless')
    chrome=webdriver.Chrome(chrome_options=chrome_options)
    chrome.get(url)
    chrome.implicitly_wait(3)
    try:
        #找到搜索栏
        key_input=chrome.find_element_by_id('key')
        #输入搜索关键字
        key_input.send_keys(keyword)
        #回车搜索
        key_input.send_keys(Keys.ENTER)
        #根据搜索条件获取产品页
        get_goods(chrome)
    finally:
        chrome.close()


def get_goods(chrome):
    try:
        #所有关于python的商品信息在div id为J_goodList列,ul下所有li为商品信息
        goods=chrome.find_elements_by_class_name('gl-item')
        #遍历循环每个商品li，并取出相关信息
        for good in goods:
            #详情页面
            g_deail_url=good.find_element_by_tag_name('a').get_attribute('href')
            g_name=good.find_element_by_css_selector('.p-name em').text.replace('\n','')
            g_price=good.find_element_by_css_selector('.p-price i').text
            g_commit=good.find_element_by_css_selector('.p-commit a').text

            msg='''
            商品名称:%s
            商品详情:%s
            商品价格:%s
            评论数量:%s
            ''' %(g_name,g_deail_url,g_price,g_commit)
            print(msg,end='\r\n')
        button=chrome.find_element_by_partial_link_text('下一页')
        button.click()
        time.sleep(2)
        get_goods(chrome)

    except Exception as e:
        print(e)
    finally:
        chrome.close()


if __name__=='__main__':
    url='https://www.jd.com'
    keyword='python'
    spider(url,keyword)


#结果
'''
  商品名称:【正版包邮】Python与量化投资从基础到实战 编程从入门到实践 基础教程书
            商品详情:https://item.jd.com/29414481402.html
            商品价格:63.40
            评论数量:20+


            商品名称:Python高级编程
            商品详情:https://item.jd.com/11017782906.html
            商品价格:34.90
            评论数量:10+


            商品名称:Python网络爬虫从入门到实践 计算机与互联网 编程语言与程序设计 零基础自学编程
            商品详情:https://item.jd.com/26728885072.html
            商品价格:48.30
            评论数量:10+


            商品名称:Python测试之道 Python3.6测试开发实战指南书籍
            商品详情:https://item.jd.com/29196914461.html
            商品价格:41.80
            评论数量:30+


            商品名称:Python编程快速上手 让繁琐工作自动化
            商品详情:https://item.jd.com/27537241701.html
            商品价格:38.00
            评论数量:2


            商品名称:流畅的Python/图灵程序设计丛书
            商品详情:https://item.jd.com/12607788862.html
            商品价格:100.08
            评论数量:7


            商品名称:数据科学导论：Python语言实现（原书第2版）
            商品详情:https://item.jd.com/12330225.html
            商品价格:59.00
            评论数量:50+
            ......
'''