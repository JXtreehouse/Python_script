#-*- encoding:utf-8 -*-
# https://github.com/letiantian/Flask-dashboard-for-UPYUN

__author__ = 'AlexZ33'

import upyun
import upyun2
import time
import re

def valid_login(bucket, username, password):
    """
    判断试图登录用户信息是否存在
    :param bucket:
    :param username:
    :param password:
    :return:
    """
    try:
        bucket = upyun2.UpYun2(bucket, username, password, timeout=10, endpoint=upyun.ED_AUTO)
        bucket.getinfo('/') # 若无法获取信息，则可能是用户信息错误
        return True