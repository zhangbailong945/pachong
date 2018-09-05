#淘宝网自动完成搜索

import sys
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

chrome_options=Options()
#chrome_options.add_argument('--headless')

chrome=webdriver.Chrome()
chrome.get('https://world.taobao.com/')
wait=WebDriverWait(chrome,5)


try:
    #淘宝首页搜索栏
    input_tag=wait.until(EC.presence_of_element_located((By.ID,'mq')))
    input_tag.send_keys('python入门')
    #搜索按钮
    search_btn=chrome.find_element_by_xpath('//*[@id="J_PopSearch"]/div[1]/div/form/input[2]')
    search_btn.click()
    time.sleep(5)
finally:
    chrome.close()

