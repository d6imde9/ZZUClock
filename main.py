#coding:utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

chromedriver = "/usr/bin/chromedriver" #浏览器驱动配置
os.environ["webdriver.chrome.driver"] = chromedriver
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-gpu')
option.add_argument("blink-settings=imagesEnabled=false")
option.add_argument('--disable-dev-shm-usage')
option.add_argument('--ignore-certificate-errors')
option.add_argument("--disable-extensions")
prefs = {"profile.default_content_setting_values.geolocation" :2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=option, executable_path=chromedriver) #启动浏览器

account = os.environ.get('ACCOUNT').split(';') #字符串预处理
errors = 0

for acc in account:
    usr = acc.split(',')
    #进入登陆界面，输入学号和密码进行登录
    driver.get('https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0')
    driver.find_element(by=By.NAME, value='uid').send_keys(usr[0])
    driver.find_element(by=By.NAME, value='upw').send_keys(usr[1])
    driver.find_element(by=By.NAME, value='myform52').submit()
    if driver.current_url == 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login':
        print('登录失败')
        errors += 1
    else: #进入信息确认界面，点击“本人填报”
        frame = driver.find_element(by=By.NAME, value='zzj_top_6s')
        driver.switch_to.frame(frame)
        
        if driver.find_element(by=By.XPATH, value='//*[@id="bak_0"]/div[5]/span').text == "今日您已经填报过了":
            print("已填报")
        else: #进入打卡界面，点击“提交表格”
            driver.find_element(by=By.XPATH, value='//*[@id="bak_0"]/div[11]/div[3]/div[4]').click()
            driver.find_element(by=By.XPATH, value='//*[@id="btn416b"]').click()
            
            res = driver.find_element(by=By.XPATH, value='//*[@id="bak_0"]/div[2]/div[2]/div[2]/div[2]').text
            if "同学，感谢你今日上报健康状况" not in res:
                errors += 1
            print(res, '\n')
driver.close()

try:
    if errors > 0:
        raise Exception("打卡失败")
except Exception:
    print(errors)
else:
    print("打卡完成")
