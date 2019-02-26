# -*- coding:utf-8 -*-
#日志类
import logging
import os.path
import time

class Logger(object):

    def __init__(self,logger):
        """
           指定保存日志的文件路径，日志级别以及调用文件
           将日志存入到指定文件中
           """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler，用于写入日志文件
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        current_time = time.strftime('%Y%m%d-%H%M',time.localtime(time.time()))
        log_name = log_path + current_time + '.log'
        file_handler = logging.FileHandler(log_name,encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        #再创建一个handler，用于输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        #定义handler的输出格式
        handler_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(handler_formatter)
        console_handler.setFormatter(handler_formatter)

        #给logger添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def getlog(self):
        return self.logger