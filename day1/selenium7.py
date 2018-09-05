#动作链
import sys
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

chrome=webdriver.Chrome()
chrome.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#wait=WebDriverWait(chrome,5)
chrome.implicitly_wait(5)

try:
    chrome.switch_to.frame('iframeResult') ##切换到iframeResult
    source=chrome.find_element_by_id('draggable')
    target=chrome.find_element_by_id('droppable')
    #1、基于同一个动作链串行执行
    #actions=ActionChains(chrome) #拿到动作链对象
    #actions.drag_and_drop(source,target) #把动作放到动作链中，准备串行执行
    #actions.perform()
    #2、不同动作链，每次移动的位移都不同
    ActionChains(chrome).click_and_hold(source).perform()
    distance=target.location['x']-source.location['x']

    track=0
    while track<distance:
        ActionChains(chrome).move_by_offset(xoffset=2,yoffset=0).perform()
        track+=2
    ActionChains(chrome).release().perform()


    time.sleep(10)
finally:
    chrome.close()