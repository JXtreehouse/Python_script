#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/10/19
# @Author : AlexZ33
# @Site : 批量给pdf文件添加满屏水印 http://www.redicecn.com/html/Python/20130101/441.html
# @File : create_waterware.py
# @Software: PyCharm


import os
import sys
import math
import textwrap

# http://pybrary.net/pyPdf/
from PyPDF2 import PdfFileReader,PdfFileWriter
from copy import copy

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase.ttfonts import TTFont



# 获取文件路径

path = os.getcwd()

# 文件读取
"""创建PDF水印模板 """
def create_watermark(
        content,
        rotate=45,
        N_space_between_content=5,
        alpha=0.3,
        fontsize =12,
        Font = 'SimHei'
):
    # 使用reportlab来创建一个PDF文件来作为一个水印文件
    c = canvas.Canvas('watermark.pdf')
    c.setFont(Font, fontsize)
    c.setFillAlpha(alpha)
    c.rotate(rotate)
    c.save()