import sys,time,logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




#根据小说名搜索
def scrapy(url,keyword):
    chrome_options=Options()
    chrome_options.add_argument('--headless')
    chrome=webdriver.Chrome(chrome_options=chrome_options)
    #chrome=webdriver.Chrome()
    chrome.get(url)
    #隐式等待
    chrome.implicitly_wait(3)
    try:
        #找到搜索栏
        search_input=chrome.find_element_by_id('wd')
        search_input.send_keys(keyword)
        #回车搜索
        search_input.send_keys(Keys.ENTER)

        get_result(chrome)
    except Exception as e:
        print(e)
    finally:
        chrome.close()


def get_result(chrome):
    chrome.implicitly_wait(3)
    try:
        #小说详情页
        book_title=chrome.find_element_by_xpath('//*[@id="info"]/h1').tag_name
        print(book_title)
    except Exception as e:
        print(e)
    finally:
        chrome.close()



def get_novel():
    pass


if __name__=='__main__':
    url='http://www.huanyue123.com/'
    keyword='牧神记'
    scrapy(url,keyword)

