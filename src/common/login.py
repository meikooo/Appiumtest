# coding=utf-8
import time
import warnings

from appium import webdriver
from logger import logger

from MethodObject.swipe import swipLeft

desired_caps = {
        'platformName': 'Android',
        'deviceName': 'SWKNSOKVOVBE7P69',
        'platformVersion': '4.4.4',
        # apk包名
        'appPackage': 'com.glodon.cp.view',
        # apk的launcherActivity
        'appActivity': 'com.glodon.cp.activity.StartActivity',
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


warnings.simplefilter("ignore", ResourceWarning)
time.sleep(3)
swipLeft(driver,n=3)
driver.find_element_by_id('com.glodon.cp.view:id/startBtn').click()
time.sleep(2)
driver.find_element_by_id('com.glodon.cp.view:id/login_username').send_keys(u"1")
driver.find_element_by_id('com.glodon.cp.view:id/login_password').send_keys(u"A")
time.sleep(1)
driver.find_element_by_id("com.glodon.cp.view:id/login_login_btn").click()
time.sleep(3)
driver.find_element_by_id("com.glodon.cp.view:id/common_titlebarleft_btn").click()
leftuser = driver.find_element_by_id("com.glodon.cp.view:id/slidingmenu_leftuser_tv").text
logger.info(u"成功获取"+leftuser)
time.sleep(2)
try:
    assert leftuser in "Ren的空间列表"
    logger.info(u"登录成功")
except Exception as e:
    logger.error(u"登录失败")
