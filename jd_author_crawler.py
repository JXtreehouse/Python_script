# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt

# import numpy as np

# 抓取页面
def get_page(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/ 20100101 Firefox/66.0")
    return urllib.request.urlopen(req, timeout=15).read()

def main():
    url = "https://list.jd.com/list.html?cat=1713,3258,3304&page=1&sort=sort_totalsales15_desc&trans=1&JL=4_2_0#J_main"
    text = get_page(url)
    # 读取
    open("out.html", "wb").write(text)
    # decode转换为字符串
    text = text.decode('utf-8')
    # 放入Beautifulsoup解析
    root = BeautifulSoup(text, 'html.parser')
    # 计算数量的字典
    author = {}
    # 寻找节点
    for item in root.find_all(class_ = )
