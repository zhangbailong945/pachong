# 模拟浏览器前进 后台
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

browser=webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.tmall.com')
browser.get('https://world.taobao.com')

browser.back()
time.sleep(10)
browser.forward()
browser.close()

#baidu
#tamll
#tabao
#tamll
#taobao




