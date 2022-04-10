#coding:utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

account = os.environ.get('ACCOUNT').split(';')

chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-gpu')
option.add_argument('--disable-dev-shm-usage')

if __name__ == '__main__':
    for acc in account:
        usr = acc.split(',')
        driver = webdriver.Chrome(options=option, executable_path=chromedriver)
        driver.get('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0')
        driver.find_element(by=By.NAME, value='uid').send_keys(usr[0])
        driver.find_element(by=By.NAME, value='upw').send_keys(usr[1])
        driver.find_element(by=By.NAME, value='myform52').submit()
        
        frame = driver.find_element(by=By.NAME, value='zzj_top_6s')
        driver.switch_to.frame(frame)
        driver.find_element(by=By.XPATH, value='//*[@id="bak_0"]/div[11]/div[3]/div[4]').click()
        
        sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="btn416a"]').click()
        
        res = driver.find_element(by=By.XPATH, value='//*[@id="bak_0"]/div[2]/div[2]/div[2]/div[2]').text
        print(res, '\n')
        driver.close()
    
