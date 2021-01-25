#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/22
# @Author : AlexZ33
# @Site :  写一个函数，根据具体国家名返回pygal提供的两位国别码
# @File : country_codes.py
# @Software: PyCharm
from pygal_maps_world.i18n import COUNTRIES


# import warnings
# warnings.filterwarnings("ignore")
def get_country_code(country_name):
    for code, name in COUNTRIES.items():

        if name == country_name:  # 不满足if语句，然后不执行
            return code  # 在循环中return返回值，然后退出循环
    return None
