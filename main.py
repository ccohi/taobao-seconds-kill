# 导入模块
"""
本软件适用于python3.10以上版本
需要安装适配edge版本的包
下方链接可以查询到相关版本自动化包：
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
"""
import datetime
import time
import win32com.client
from selenium import webdriver
from selenium.webdriver.common.by import By


speaker = win32com.client.Dispatch("SAPI.SpVoice")

# 抢购时间，需要校对电脑时间和阿里时间是否相同
times = '2022-10-31 20:00:00'
browser = webdriver.Edge()
browser.get("https://www.taobao.com")

time.sleep(3)
browser.find_element(By.LINK_TEXT, "亲，请登录").click()
print(f"登录成功")

time.sleep(20)
browser.get("https://cart.taobao.com/cart.htm")

while 1 == 1:
    # 找到全选框
    if browser.find_element(By.CSS_SELECTOR, "#J_SelectAll2"):
        browser.find_element(By.CSS_SELECTOR, "#J_SelectAll2").click()
        print("找到全选")
        break

while 1 == 1:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now)
    # 点击清空购物车按钮
    if now > times:
        while 1 == 1:
            try:
                if browser.find_element(By.CSS_SELECTOR, "#J_SmallSubmit"):
                    print("找到点击位置")
                    browser.find_element(By.CSS_SELECTOR, "#J_SmallSubmit").click()
                    print("已抢到")
                    break
            except:
                pass

    # 点击立即支付
    if now > times:
        while 1 == 1:
            try:
                if browser.find_element(By.CLASS_NAME, "go-btn"):
                    browser.find_element(By.CLASS_NAME, "go-btn").click()
                    break
            except:
                pass

