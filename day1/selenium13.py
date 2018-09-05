#selenium异常处理
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException,NoSuchFrameException


try:
    chrome=webdriver.Chrome()
    chrome.get('https://www.baidu.com')
    chrome.switch_to.frame('iframssseResult')
except TimeoutException as e:
    print(e)
except NoSuchFrameException as e:
    print(e)
finally:
    chrome.close()