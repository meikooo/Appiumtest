# coding:utf-8
import configparser
import time
import unittest
import warnings


from appium import webdriver

from MethodObject.logger import Logger
from MethodObject.swipe import *


desired_caps = {
                'platformName': 'Android',
                'deviceName': 'SWKNSOKVOVBE7P69',
                'platformVersion': '4.4.4',
                # apk包名
                'appPackage': 'com.glodon.cp.view',
                # apk的launcherActivity
                'appActivity': 'com.glodon.cp.activity.StartActivity',
                'unicodeKeyboard':True,
                'resetKeyboard':True
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

logger = Logger(logger="login").getlog()


class lanchApp(unittest.TestCase):

    config = configparser.ConfigParser()
    config.read("F:\\个人文档\\code\\Kumapocket\\config\\config.ini")
    username = config.get("userName", "userName")
    password = config.get("passWord", "PassWord")

    def test_login(self,username = username,password = password):
        warnings.simplefilter("ignore", ResourceWarning)

        time.sleep(5)
        swipLeft(driver, n=3)
        driver.find_element_by_id('com.glodon.cp.view:id/startBtn').click()
        time.sleep(5)
        driver.find_element_by_id('com.glodon.cp.view:id/login_username').send_keys(username)
        driver.find_element_by_id('com.glodon.cp.view:id/login_password').send_keys(password)
        time.sleep(5)
        driver.find_element_by_id("com.glodon.cp.view:id/login_login_btn").click()
        time.sleep(3)
        driver.find_element_by_id("com.glodon.cp.view:id/common_titlebarleft_btn").click()
        leftuser = driver.find_element_by_id("com.glodon.cp.view:id/slidingmenu_leftuser_tv").text
        logger.info(u"成功获取"+leftuser)
        time.sleep(3)
        try:
            assert leftuser in "Ren的空间列表"
            logger.info(u"登录成功")
        except Exception as e:
            logger.error(u"登录失败")

if __name__ == '__main__':
    unittest.main()
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    driver.get_screenshot_as_file(u"E:\\Appiumtest\\screenshots\\登录成功"+current_time+".png")
