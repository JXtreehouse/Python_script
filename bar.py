#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/20
# @Author : AlexZ33
# @Site : 
# @File : bar.py
# @Software: PyCharm

import pygal

bar_chart = pygal.HorizontalStackedBar()
bar_chart.title = "Remarkable sequences"
bar_chart.x_labels = map(str, range(11))
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
bar_chart.render_to_file("HorizontalStackedBar-add-labels.svg")
