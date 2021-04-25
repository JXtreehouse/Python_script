#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/22
# @Author : AlexZ33
# @Site :  更多地图可视化可看这篇：https://blog.csdn.net/qq_46614154/article/details/106255835?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1.control
# @File : world_population_map.py
# @Software: PyCharm

import json
import os
from country_codes import get_country_code
from pygal_maps_world.maps import World
# 颜色相关
from pygal.style import RotateStyle,LightColorizedStyle


path = os.getcwd()
filename = path + '/data/worldpopulation.json'

with open(filename) as f:
    # json.load()可以将json文件转为Python能处理的形式，这里位列表，列表里是字典
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:  # 将每个字典(上面解释的用大括号包裹的4个键值对)存储在pop_dict中
    if pop_dict['Year'] == '2010':  # for循环是一次操作一个值
        country_name = pop_dict['Country Name']
        # 有些值是小数，先转为float再转为int
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        print(country_name + ': ', population)
        if code:
            cc_populations[code] = population          #字典的赋值
        else:
            print("ERROR"+":"+country_name)
# 为了使颜色分层更加明显
cc_populations_1, cc_populations_2, cc_populations_3 = {}, {}, {}
for cc, population in cc_populations.items():
    if population < 10000000:
        cc_populations_1[cc] = population
    elif population < 1000000000:
        cc_populations_2[cc] = population
    else:
        cc_populations_3[cc] = population

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
world = World(style=wm_style)
world.title = 'World Populations in 2010, By Country'
world.add('0-10m', cc_populations_1)
world.add('10m-1bn', cc_populations_2)
world.add('>1bn', cc_populations_3)
world.render_to_file('world_population_2010.svg')
world.render_in_browser()