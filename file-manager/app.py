#-*- encoding:utf-8 -*-

__author__ = 'AlexZ33'

from flask import Flask, request, session, redirect, url_for, render_template, escape, Response

import upyun
import upyun2
import util
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024

app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'

@app.route('/', methods = ['POST', 'GET'])
def index():
    