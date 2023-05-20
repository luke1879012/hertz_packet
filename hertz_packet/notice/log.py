# -*- coding: utf-8 -*-

"""
@Project : hertz_packet 
@File    : log.py
@Date    : 2023/5/19 17:56:47
@Author  : zhchen
@Desc    : 
"""
import logging
from logging import FileHandler

def setup_logger(log_file):
    # 创建日志器
    logger = logging.getLogger('backup_logger')
    logger.setLevel(logging.INFO)

    # 创建文件处理程序
    file_handler = FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # 创建日志格式器
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # 将文件处理程序添加到日志器
    logger.addHandler(file_handler)

    return logger