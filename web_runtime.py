#!/usr/local/bin/python3
# coding=utf-8
# 一个简单的web ide for python
import sys


def check_version():
    """python版本检测"""
    v = sys.version_info
    if v.major == 3 and v.minor >= 4:
        return True
    print('Your current python is %d.%d. Please use Python3.4' % (v.major, v.minor))
    return False


if not check_version():
    exit(1)

import os, io, json, subprocess, tempfile,signal, time
from urllib import parse
from wsgiref.simple_server import make_server

XEC = sys.executable
PORT = 9090
HOST = 'localhost:%d' % PORT
TEMP = tempfile.mkdtemp(suffix='_py', prefix='learn_python_')
INDEX = 0

def main():
    httpd = make_server('127.0.0.1', PORT, application)
    print()
