
from MethodObject.logger import Logger
from config.config import *

logger = Logger(logger="baseLog").getlog()
logger.info('开始从配置文件中获取测试相关的配置')

def make_dis():
    dis_app={}
    dis_app['platformName'] = platformName
    dis_app['platformVersion'] = platformVersion
    dis_app['deviceName'] = deviceName
    dis_app['appPackage'] = appPackage
    dis_app['appActivity'] =appActivity
#   dis_app['androidDeviceReadyTimeout'] =androidDeviceReadyTimeout
    dis_app['unicodeKeyboard'] = unicodeKeyboard
    dis_app['resetKeyboard'] =resetKeyboard
    return  dis_app