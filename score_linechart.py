#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/20
# @Author : AlexZ33
# @Site : 
# @File : score_linechart.py
# @Software: PyCharm
import pygal
line_chart = pygal.Line()
line_chart.title = '希文小朋友各科成绩趋势图'
line_chart.x_labels = map(str, range(1, 6))
# temp = map(str, range(1, 6))
# print(temp)
line_chart.add('数学', [66, 58, 70, 72,76, 78])
line_chart.add('语文', [88, 89, 90, 88, 86, 82])
line_chart.add('英语', [98, 99, 99, 96, 100, 98])

line_chart.render_in_browser()

