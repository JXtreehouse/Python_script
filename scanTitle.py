"""
  批量获取域名标题 scanTitle.py urls.txt 10 (线程)
"""
import sys
import requests
import threading
import re
import math
import time
import os
from requests.packages.urllib3.exception import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def getUrls(filename):
    f = open(filename, 'r', encoding='utf8')
    lines = f.readlines()
    urls = [url.strip() for url in lines]
    return urls

def check_http(target):
    """检测目标是否为http服务"""
    target = target.strip()
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)"
    }
    try:
        url = "%s:"