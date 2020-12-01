#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/1
# @Author : AlexZ33
# @Site : 
# @File : pillow_img_save.py
# @Software: PyCharm
from PIL import Image
im = Image.open('./img/xinyuan.jpg')
print(im)
im.save("./img/xinyuan.png")     ## 将"./img/xinyuan.jpg"保存为"./img/xinyuan.png"
im = Image.open("./img/xinyuan.png")  ##打开新的png图片
print(im.format, im.size, im.mode)