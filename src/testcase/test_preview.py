from appium import webdriver
import os
import unittest
import time

from MethodObject.logger import Logger

import warnings
from src.common.login import *
from MethodObject.swipe import *
import uiautomator


logger = Logger(logger="documentPreview").getlog()

class documentPreview(unittest.TestCase):

    def test_documentPreview(self):
        warnings.simplefilter("ignore", ResourceWarning)
        time.sleep(3)
        #swipeUp(driver, n=1)
        #driver.find_element_by_android_uiautomator('new UiSelector().text(\"13795291583的空间\")').text

        time.sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text(\"EL394A7A5E-BIMM\"').click()
        time.sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text(\"001-自动化测试\"').click()
        time.sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text(\"04-文件预览\"').click()
        time.sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text(\"1-1多页WORD-迭代总结.docx\"').click()
        time.sleep(5)
        current_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file(u"E:\\Appiumtest\\screenshots\\预览页-owa" + current_time + ".png")
        driver.find_element_by_android_uiautomator('new UiSelector().text(\"返回\"').click()
        logger.info('owa文件预览完毕')

if __name__ == '__main__':
    unittest.main()
