#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/12
# @Author : AlexZ33
# @Site : https://jingyan.baidu.com/article/fb48e8be37b6696e622e14db.html
# https://www.cnblogs.com/saryli/p/5050038.html
# @File : change_file_name.py
# @Software: PyCharm
# @descript: 如何用python批量改文件名

# 引入os模块（python中操作文件的模块）。
import os;
import re;


# 定义修改名称的函数rename。
# 在rename函数中定义一个储存路径的变量path，并将要修改文件名的文件夹的路径赋值给该变量。

def rename():
    path = "/home/mi/下载"
    re.match()
    fileList = os.listdir(path)  # 该文件夹下所有的文件(包括文件夹)
    for file in fileList: #遍历所有文件+
        olddir = os.path.join(path, file) # 原来的文件路径
        if os.path.isdir(olddir): # 如果是文件夹则跳过
            continue;
        filename = os.path.splitext(file)[0];# 文件名
        getresumename = filename
        text = os.path.splitext(file)
        filetype = os.path.splitext(file)[1]; # 文件扩展名
        newdir = os.path.join(path, '【内部推荐】社招-{name}-内推人{filetype}'.format(name= filename, filetype=filetype))
        print(newdir)


rename()

