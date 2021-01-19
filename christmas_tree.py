#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/19
# @Author : AlexZ33
# @Site : 
# @File : christmas_tree.py
# @Software: PyCharm

import turtle
import time
screen = turtle.Screen()
screen.setup(375, 700)

circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()

square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()

circle.goto(0, 280)
circle.stamp()

k = 0
for i in range(1, 13):
    y = 30 * i
    for j in range(i - k):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()

    if i % 4 == 0:
        x = 30 * (j + 1)
        circle.color('red')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()
        k += 3

    if i % 4 == 3:
        x = 30 * (j + 1)
        circle.color('yellow')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()

square.color('brown')
for i in range(13, 17):
    y = 30 * i
    for j in range(2):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(-120, 270)
text.color('red')
text.write('圣诞快乐', font=('SimHei', 18, 'bold'))
# 可以把【圣诞快乐】换成你的祝福语哦~」
time.sleep(60)

