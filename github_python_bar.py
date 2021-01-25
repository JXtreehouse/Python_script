#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/25
# @Author : AlexZ33
# @Site : 
# @File : github_python_bar.py
# @Software: PyCharm
import requests

import pygal
from pygal.style import LightColorizedStyle, LightenStyle

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
# 200为响应成功
print(response.status_code, '响应成功！')
response_dict = response.json()

total_repo = response_dict['total_count']
repo_list = response_dict['items']
print('总仓库数: ', total_repo)
print('top', len(repo_list))

# 在图表中添加可单击的链接
# 在为每个项目创建的字典中，只需添加一个键为’xlink’的键-值对
names, plot_dicts = [], []
for repo_dict in repo_list:
    names.append(repo_dict['name'])
    # 加上str强转，因为我遇到了'NoneType' object is not subscriptable (: 说明里面有个没有此项, 是NoneType
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        # 有些描述很长很长，选最前一部分
        'label': str(repo_dict['description'])[:200] + '...',
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 改变默认主题颜色，偏蓝色
my_style = LightenStyle('#333366', base_style=LightColorizedStyle)
# 配置: 我们创建了一个Pygal类Config实例，命名为my_config
my_config = pygal.Config()
# 在这个图表中，副标签是x轴上的项目名&y轴上的大部分数字
# x轴的文字旋转45度
my_config.x_label_rotation = -45
# 隐藏左上角的图例
my_config.show_legend = False
# 标题字体大小
my_config.title_font_size = 30
# 副标签，包括x轴和y轴大部分
my_config.label_font_size = 20
# 主标签是y轴某数倍数，相当于一个特殊的刻度，让关键数据点更醒目
# 这些刻度应更大，以与副标签区分开
my_config.major_label_font_size = 24
# 限制字符为15个，超出的以...显示
# truncate_label将较长的项目名缩短为15个字符（如果将鼠标指向被截短的项目名，将显示完整的项目名）
my_config.truncate_label = 15
# 不显示y参考虚线
# show_y_guides=False以隐藏图表中的水平线
my_config.show_y_guides = False
# 图表宽度
# 最后自定义了宽度，让图表更充分地利用浏览器地可用空间
my_config.width = 1000

# 第一个参数可以传配置
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
# x轴的数据
chart.x_labels = names
# 加入y轴的数据，无需title设置为空，注意这里传入的字典，
# 其中的键--value也就是y轴的坐标值了
chart.add('', plot_dicts)
chart.render_to_file('most_stars_python_repo.svg')
chart.render_in_browser()