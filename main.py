#coding:utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

account = os.environ.get('ACCOUNT').split(';') #字符串预处理
mail = os.environ.get('MAIL', 'none')

chromedriver = "/usr/bin/chromedriver" #浏览器驱动配置
os.environ["webdriver.chrome.driver"] = chromedriver
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-gpu')
option.add_argument('--disable-dev-shm-usage')

if __name__ == '__main__':
    driver = webdriver.Chrome(options=option, executable_path=chromedriver) #启动浏览器
    for acc in account:
        usr = acc.split(',')
        
        #进入登陆界面，输入学号和密码进行登录
        driver.get('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0')
        driver.find_element(by=By.NAME, value='uid').send_keys(usr[0])
        driver.find_element(by=By.NAME, value='upw').send_keys(usr[1])
        driver.find_element(by=By.NAME, value='myform52').submit()
        if driver.current_url == 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login': #登陆失败
            res = driver.find_element(by=By.XPATH, value='//*[@id="bak_0"]/div[2]/div[2]/div[2]/div[2]').text
            print(res, '\n')
            continue
        
        #进入信息确认界面，点击“本人填报”
        frame = driver.find_element(by=By.NAME, value='zzj_top_6s')
        driver.switch_to.frame(frame)
        driver.find_element(by=By.XPATH, value='//*[@id="bak_0"]/div[11]/div[3]/div[4]').click()
        
        #进入打卡界面，点击“提交表格”
        sleep(2)
        driver.find_element(by=By.XPATH, value='//*[@id="btn416b"]').click()
        
        res = driver.find_element(by=By.XPATH, value='//*[@id="bak_0"]/div[2]/div[2]/div[2]/div[2]').text
        print(res, '\n')
     driver.close()
    
