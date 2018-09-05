#当前网页内嵌的iframe
import sys,time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

try:
    chrome=webdriver.Chrome()
    chrome.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    chrome.switch_to.frame('iframeResult') #切换到id为iframeResult的frame
    tag1=chrome.find_element_by_id('droppable')
    print(tag1)
    #报错，在子frame里无法查看到父frame的元素
    #tag2=chrome.find_element_by_id('textareaCode')
    #切换回父frame，就可以找到了
    chrome.switch_to.parent_frame()
    tag2=chrome.find_element_by_id('textareaCode')
    print(tag2.tag_name)
    print(tag2.text)
finally:
    chrome.close()