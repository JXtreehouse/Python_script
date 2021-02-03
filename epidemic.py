#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/1
# @Author : AlexZ33
# @Site : 2019-nCov疫情数据爬虫
# @reference:https://github.com/viniciuschiele/flask-apscheduler
# @File : epidemic.py
# @Software: PyCharm

from flask import Flask
from datetime import datetime
import requests
import pymysql
import logging
import os
import json

"""
pip3 install Flask-APScheduler
"""
from flask_apscheduler import APScheduler

LOG_DIR = './logs'
if not os.path.isdir(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
handler = logging.FileHandler(os.path.join(LOG_DIR, 'log.log'))
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - [Rel]%(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Config(object):  # 创建配置类
    # 任务列表
    JOBS = [
        # {  # 第一个任务
        #     'id': 'job1',
        #     'func': '__main__:job_1',
        #     'args': (1, 2),
        #     'trigger': 'cron', # cron表示定时任务
        #     'hour': 19,
        #     'minute': 27
        # },
        {  # 第二个任务，每隔600S执行一次
            'id': 'job2',
            'func': '__main__:get_epidemic_data',  # 方法名
            'trigger': 'interval',  # interval表示循环任务
            'seconds': 600,
        }
    ]


def json2sql_str(json):
    keys = ",".join(json.keys())
    values = ",".join([
        str(v) if
        (isinstance(v, int) or (isinstance(v, float))) else "'" + str(v) + "'"
        for v in json.values()
    ])
    return keys, values


province = []
city = []
world = []


def get_epidemic_data():
    global province, city, world
    try:
        host = 'localhost'
        port = 3306
        user = 'datav'
        passwd = 'datav'
        db = 'epidemic'
        t_last = ''
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=passwd,
            database=db,
        )
        cursor = conn.cursor()
        SQL_PROVINCE = """INSERT INTO prov_data(%s) VALUES (%s)"""
        SQL_CITY = """INSERT INTO city_data(%s) VALUES (%s)"""
        SQL_WORLD = """INSERT INTO world_data (%s) VALUES (%s)"""

        cursor.execute("SELECT time_txt FROM world_data ORDER BY load_time DESC LIMIT 1")
        res = cursor.fetchall()
        if len(res):
            t_last = res[0][0]
        r = requests.get('https://interface.sina.cn/news/wap/fymap2020_data.d.json')
        js = r.json()

        t = js['data']['times']
        if t_last != t:
            ls = js['data']['list']
            wls = js['data']['worldlist']
            prov_data = []
            city_data = []
            world_data = []
            sqls_prov = []
            sqls_city = []
            sqls_world = []
            for l in ls:
                prov = l['name']
                prov_diag = l['value']
                prov_sus = int(l['susNum'])
                prov_cure = int(l['cureNum'])
                prov_death = int(l['deathNum'])
                prov_data.append({
                    'prov': prov,
                    'diag': prov_diag,
                    'sus': prov_sus,
                    'cure': prov_cure,
                    'death': prov_death,
                    'time_txt': t
                })
                ks, vs = json2sql_str(prov_data[-1])
                sqls_prov.append(SQL_PROVINCE % (ks, vs))
                cursor.execute(sqls_prov[-1])
                for c in l['city']:
                    city = c['name']
                    city_diag = c['conNum']
                    city_sus = c['susNum']
                    city_cure = c['cureNum']
                    city_death = c['deathNum']
                    city_data.append({
                        'prov': prov,
                        'city': city,
                        'diag': city_diag,
                        'sus': city_sus,
                        'cure': city_cure,
                        'death': city_death,
                        'time_txt': t
                    })
                    ks, vs = json2sql_str(city_data[-1])
                    sqls_city.append(SQL_CITY % (ks, vs))
                    cursor.execute(sqls_city[-1])

            for wl in wls:
                world = wl['name']
                world_diag = wl['value']
                world_sus = int(wl['susNum'])
                world_cure = int(wl['cureNum'])
                world_death = int(wl['deathNum'])
                world_data.append({
                    'contry': world,
                    'diag': world_diag,
                    'sus': world_sus,
                    'cure': world_cure,
                    'death': world_death,
                    'time_txt': t
                })
                ks, vs = json2sql_str(world_data[-1])
                sqls_world.append(SQL_WORLD % (ks, vs))
                cursor.execute(sqls_world[-1])
            conn.commit()
            cursor.close()
            conn.close()
            logger.info('update_time: %s' % t)
            prov = prov_data
            city = city_data
            world = world_data

        else:
            logger.info('no update')

    except Exception as e:
        logger.warn('get epidemic data error, %s' % e)


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def hello_world():
    return json.dumps(city)


if __name__ == '__main__':
    logger.info('start')
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=False, host='0.0.0.0', port=8000)
