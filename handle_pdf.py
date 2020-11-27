#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25
# @Author : AlexZ33　白鲸鱼
# @Site : https://weread.qq.com/web/reader/7993218071e524ec799ab46k1c932da029c1c9ac015999a
# @File : handle_pdf.py
# 问题列表: https://blog.csdn.net/weixin_39278265/article/details/84799843
# @description: python操作PDF文件
# @Software: PyCharm

import PyPDF2

fn = './data/大数据时代.pdf'  # 指定读取文件的路径
fn_protected = './data/大数据时代-protected.pdf'

# pageObj = pdfRd.getPage()  # 将第10页内容读入pageObj
# txt = pageObj.extractText()
# print(txt)

"""
检查PDF是否被加密
目录　./data/大数据时代.pdf　文件没有加密
目录

"""
#
#
# def encryptYorN(fn):
#     """检查文件是否加密"""
#     pdfObj = open(fn, 'rb')  # 'rb'表示以二进制打开
#     # print(pdfObj)
#
#     pdfRd = PyPDF2.PdfFileReader(pdfObj)  # 读取文件
#     # print("PDF页数= ", pdfRd.numPages)
#
#     if pdfRd.isEncrypted:  # 由这个属性判断是否加密
#         print("%s 文件有加密" % fn)
#     else:
#         print("%s 文件没有加密" % fn)
#
#
# encryptYorN(fn)
# encryptYorN(fn_protected )

"""
对于加密的PDF文件，我们可以使用decrypt( )执行解密，如果解密成功decrypt( )会传回1，如果失败则传回0。
"""

pdfObj = open(fn_protected, 'rb')
pdfRd = PyPDF2.PdfFileReader(pdfObj)
if pdfRd.decrypt('1234'):
    pageObj = pdfRd.getPage(0)
    text = pageObj.extractText()
    print(text)
else:
    print("解密失败")
