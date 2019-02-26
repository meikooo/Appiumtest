import time


# 截图
import os


def getScreenShot(self):
    time = self.getTime()
    filename = '../jpg/ %s.png' % time
    self.driver.get_screenshot_as_file(filename)
