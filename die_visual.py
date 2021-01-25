#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/21
# @Author : AlexZ33
# @Site : 
# @File : die_visual.py
# @Software: PyCharm
from die import Die
import pygal
#创建一个D6
die = Die()

#掷几次骰子 并将结果存储在一个列表中
# 掷1000次
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)


frequencies = []
#分析结果
# 范围1~6，统计每个数字出现的次数
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)


#对结果进行可视化
# 条形图
hist = pygal.Bar()
hist.title = "掷骰子1000次6个面的出现次数"
# x轴坐标
hist.x_labels = ['1','2','3','4','5','6']
# x、y轴的描述
hist.x_title = "结果面"
hist.y_title = "次数"
# 添加数据， 第一个参数是数据的标题
hist.add("D6",frequencies)

# hist.render_to_file("die_visual.svg")

# hist.render_to_png("die_visual.png")
# 使用浏览器打开
hist.render_in_browser()