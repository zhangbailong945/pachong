import sys,time,hashlib,logging

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
DATA_FORMAT="%m/%d%Y %H:%M:%S %p"
logging.basicConfig(level=logging.INFO,format=LOG_FORMAT,datefmt=DATA_FORMAT)

chrome=webdriver.Chrome()
try:
    chrome.get('https://mail.qq.com')
    wait=WebDriverWait(chrome,5)
    login_frame=wait.until(EC.presence_of_element_located((By.ID,'login_frame')))
    chrome.switch_to_frame(login_frame)
    wait.until(EC.presence_of_element_located((By.ID,'login')))
    qq_user=chrome.find_element_by_name('u')
    qq_pwd=chrome.find_element_by_name('p')
    qq_user.send_keys('308808490')
    qq_pwd.send_keys('zbl_1034')
    auto_login_checked=chrome.find_element_by_id('p_low_login_enable')
    auto_login_checked.click()
    login_btn=chrome.find_element_by_id('login_button')
    login_btn.click()
    time.sleep(5)
    quit_a=wait.until(EC.presence_of_element_located((By.ID,'useralias')))
    if quit_a.text=='蓝色贝壳':
        logging.info("QQ邮箱登陆成功！")
    
    #开始写信
    wait.until(EC.presence_of_element_located((By.ID,"navBarDiv")))
    write_letter_btn=wait.until(EC.presence_of_element_located((By.ID,"composebtn")))
    write_letter_btn.click()

    #收信人
    wait=WebDriverWait(chrome,6)
    div=wait.until(EC.presence_of_element_located((By.ID,"mainFrameContainer")))
    logging.info('%s'% div.tag_name)
    frame=wait.until(EC.presence_of_element_located((By.NAME,"mainFrame")))
    chrome.switch_to_frame(frame)
    logging.info('%s'% frame.tag_name)
    wait=WebDriverWait(chrome,6)
    wait.until(EC.presence_of_element_located((By.ID,'to_btn')))
    rec_user_input=chrome.find_element_by_id("to")
    
    rec_user_input.send_keys('1207549344@qq.com')
    logging.info("收信人执行完毕")
    #标题
    title_input=chrome.find_element_by_id("subject")
    title_input.send_keys('selenium自动化测试')
    #内容
    content_input=chrome.find_element_by_name("content__html")
    logging.info('%s'% content_input.tag_name)
    content_input.send_keys("测试内容11111111111")
    #发送
    send_btn=chrome.find_element_by_name('sendbtn')
    send_btn.click()

    time.sleep(100)


except Exception as e:
    print(e)
finally:
    chrome.close()