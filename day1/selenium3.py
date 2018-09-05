import sys
from selenium import webdriver
#按照上面方式查找元素
from selenium.webdriver.common.by import By
#键盘按键操作
from selenium.webdriver.common.keys import Keys
#条件
from selenium.webdriver.support import expected_conditions as EC
#等待页面加载某些元素
from selenium.webdriver.support.wait import WebDriverWait
import time


chrome=webdriver.Chrome()
chrome.get('https://www.baidu.com')
wait=WebDriverWait(chrome,10)

try:
    #1.find_element_by_id 通过id元素对象
    #print(chrome.find_element_by_id('kw'))

    #2.find_element_by_lin_text 通过文字链接来找元素对象
    #login=chrome.find_element_by_link_text('登录')
    #login.click()

    #3.find_element_by_partial_link_text 根据部分链接文件获取元素对象
    login=chrome.find_element_by_partial_link_text('录')
    login.click()
    time.sleep(3)

    #4.find_element_by_tag_name 通过元素标签来获取元素对象
    print(chrome.find_element_by_tag_name('a'))

    #5.find_element_by_class_name 通过样式clss查找元素对象
    button=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'tang-pass-footerBarULogin')))
    button.click()
    #6.find_element_by_name
    input_user=wait.until(EC.presence_of_element_located((By.NAME,'userName')))
    input_pwd=wait.until(EC.presence_of_element_located((By.NAME,'password')))
    commit=wait.until(EC.element_to_be_clickable((By.ID,'TANGRAM__PSP_10__submit')))

    input_user.send_keys('15014927018')
    input_pwd.send_keys('zbl_1034')
    commit.click()

    #7.find_element_by_css_selector #通过css选择器获取元素对象
    print(chrome.find_element_by_css_selector('#kw'))

    #8.find_element_by_xpath #通过xpath获取元素对象


    time.sleep(6)
finally:
    chrome.close()

