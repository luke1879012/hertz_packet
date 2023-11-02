# -*- coding: utf-8 -*-

"""
@Project : hertz_packet 
@File    : goalkeeper.py
@Date    : 2023/11/2 17:02:29
@Author  : zhchen
@Desc    : 
"""
import time

from notice.goalkeeper import shooting

while True:
    result = shooting('123', 10)
    print(result)
    time.sleep(1)
