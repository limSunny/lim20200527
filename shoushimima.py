# 1. 从appium导入webdriver
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

# 2. 启动项配置
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '5.1.1'
caps['deviceName'] = '127.0.0.1:62001'
caps['app'] = r'C:\Users\lim\Desktop\19期内容\shoushimimasuo.apk'

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
time.sleep(3)
print("安装好")

driver.find_element('xpath', '//*[@text="设置手势"]').click()

print("test")