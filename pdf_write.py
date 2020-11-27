#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/26
# @Author : AlexZ33
# @Site : 
# @File : pdf_write.py.py
# @Software: PyCharm
from PyPDF2 import PdfFileReader, PdfFileWriter


def addBlankpage():
    # 注意下面是linux系统下的文件位置
    readFile = '/home/mi/personal/Python_script/data/nio.pdf'
    outFile = '/home/mi/personal/Python_script/data//copy2.pdf'
    # 注意下面是ｗｉｎｄｏｗｓ系统下的文件位置
    # readFile = 'C:/Users/Administrator/Desktop/RxJava 完全解析.pdf'
    # outFile = 'C:/Users/Administrator/Desktop/copy.pdf'

    pdfFileWriter = PdfFileWriter()

    # 获取 PdfFileReader 对象
    pdfFileReader = PdfFileReader(readFile)  # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    numPages = pdfFileReader.getNumPages()

    for index in range(0, numPages):
        pageObj = pdfFileReader.getPage(index)
        pdfFileWriter.addPage(pageObj)  # 根据每页返回的 PageObject,写入到文件
        pdfFileWriter.write(open(outFile, 'wb'))

    pdfFileWriter.addBlankPage()  # 在文件的最后一页写入一个空白页,保存至文件中
    pdfFileWriter.write(open(outFile, 'wb'))

# 注意此段代码文件过大时候无法写入
addBlankpage()
