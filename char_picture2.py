#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/1
# @Author : AlexZ33
# @Site : 
# @File : char_picture2.py
# @Software: PyCharm
from PIL import Image
img = Image.open("./img/bijini.jpg") # 打开
# img = Image.open("./img/cat.jpg") # 打开
out = img.convert("L") # 灰度
width, height = out.size # 赋值
out = out.resize((int(width * 0.2),int(height * 0.1))) # 改变图像的大小
width, height = out.size # 赋值
asciis = "@%#*+=-. "
texts  = ""
for row in range(height):
    for col in range(width):
        gray = out.getpixel((col,row))
        texts += asciis[int(gray / 255 * 8)]
    texts += "\n"
with open("bijini.txt","w") as file:
    file.write(texts)