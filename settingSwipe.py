# 1. 从appium导入webdriver
from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait


# 2. 启动项配置
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '5.1.1'
caps['deviceName'] = '127.0.0.1:62001'
caps['appPackage'] = 'com.android.settings'
caps['appActivity'] = '.Settings'
# caps['app'] = r'C:\Users\lim\Desktop\19期内容\app-debug.apk'
# caps['autoLaunch'] = False  # 不自动启动app

# 3. 连接appium服务
driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
time.sleep(3)
# 右滑driver.swipe(x1,y1,x2,y2)
size = driver.get_window_size()
print('屏幕尺寸', size)
width = size['width']
height = size['height']

x1,y1,x2,y2 = width/2, height*0.9, width/2, height*0.8

print('滑动屏幕')


def swipe_and_find(driver):
    # driver.swipe(x1,y1,x2,y2,duration=1)
    driver.flick(x1,y1,x2,y2)
    return driver.find_element('xpath', '//*[@text="关于平板电脑"]')

#循环上滑和查找
WebDriverWait(driver,30,1).until(swipe_and_find).click()

time.sleep(2)
asd = driver.find_element('xpath', '//*[@text="Android版本"]')
# driver.long_press(asd).wait(10000).perform()
for i in range(1):
    asd.click()

#add

