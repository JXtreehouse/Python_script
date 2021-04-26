#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/8 下午8:35
# @Author : AlexZ33
# @Site : 爬虫|拉接口型
# @File : huaweiGame.py http://game.vmall.com/wap/index.html?#/recomenedApp
# @Software: PyCharm
import requests
import json
import csv
import random
import time
from bs4 import BeautifulSoup

now = int(time.time())
time2 = time.localtime(now)
headers = {
    'Host': 'api.taptapdada.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}

# 声明一个列表存储字典
game_id = []
game_data = []


def get_html_text(url):
    response = requests.get(url, headers=headers)


def get_app_id():
    time.sleep(round(random.uniform(0.5, 1.5), 1))
    types = ['kindCustomTab|20|juesebanyan', 'kindCustomTab|18|dongzuosheji', 'kindCustomTab|21|qipaizhuoyou',
             'kindCustomTab|22|tiyujingsu', 'kindCustomTab|16|jingyingcelue', 'kindCustomTab|15|xiuxianyizhi']
    for type in types:
        url = 'http://game.vmall.com/wap/getTabDetail?uri={}&maxResults=25&reqPageNum=1'.format(type)
        resp = requests.get(url, headers=headers).json()
        layout_datas = resp.get('layoutData')
        if layout_datas:
            for layout in layout_datas:
                tag_name = layout.get('name')
                game_list = layout.get('dataList')[0].get('list')
                for game in game_list:
                    # game_name = game.get('name')
                    game_appid = game.get('appid')
                    # 下载安装次数
                    # game_downCountDesc = game.get('downCountDesc')
                    # game_sizeDesc = game.get('sizeDesc')
                    # game_type = game.get('logSource')
                    # game_tagName = game.get('tagName')
                    # game_versionCode = game.get('versionCode')
                    # game_appVersionName = game.get('appVersionName')
                    # game_stars = game.get('stars')
                    # game_package = game.get('package')
                    # game_data_dict = {
                    #     'game_name': game_name,
                    #     'game_appid': game_appid,
                    #     # 下载安装次数
                    #     'game_downCountDesc': game_downCountDesc,
                    #     'game_sizeDesc': game_sizeDesc,
                    #     'game_type': game_type,
                    #     'game_tagName': game_tagName,
                    #     'game_versionCode': game_versionCode,
                    #     'game_appVersionName': game_appVersionName,
                    #     'game_stars': game_stars,
                    #     'game_package': game_package,
                    # }
                    game_id.append(game_appid)
                    print(game_id)
        else:
            break


def get_game_detail():
    data_title = []
    while True:
        time.sleep(round(random.uniform(0.5, 1.5), 1))
        for appid in game_id:
            url = 'http://game.vmall.com/wap/getTabDetail?reqPageNum=1&uri=app|{}&maxResults=10'.format(appid)
            resp = requests.get(url, headers=headers).json()
            datas = resp.get('layoutData')
            if datas:
                data_list = datas[0].get('dataList')[0]
                data_list2 = datas[2].get('dataList')[0]
                # 游戏名
                name = data_list.get('name')
                # 安装次数
                intro = data_list.get('intro')
                # 评分
                stars = data_list.get('stars')

                # appid
                appid = data_list2.get('appid')
                # 包体大小
                size_desc = data_list2.get('sizeDesc')
                # 版本
                version = data_list2.get('version')
                # 时间
                releaseDate = data_list2.get('releaseDate')
                # 开发商
                developer = data_list2.get('developer')

                data_dict = {
                    'name': name,
                    'intro': intro,
                    'stars': stars,
                    'appid': appid,
                    'sizeDesc': size_desc,
                    'version': version,
                    'releaseDate': releaseDate,
                    'developer': developer
                }
                game_data.append(data_dict)
                print(game_data)
            else:
                break


def main():
    get_app_id()
    get_game_detail()
    # 将数据写入json文件
    with open('data_info.json', 'a+', encoding='utf-8-sig') as f:
        json.dump(game_id, f, ensure_ascii=False, indent=4)
    print('json文件写入完成')
    #
    # # 将数据写入csv文件
    with open('游戏信息.csv', 'w', encoding='utf-8-sig', newline='') as f:
        # 表头
        title = game_data[0].keys()
        # 创建writer
        writer = csv.DictWriter(f, title)
        # 写入表头
        writer.writeheader()
        # 批量写入数据
        writer.writerows(game_data)
    print('csv文件写入完成')


if __name__ == '__main__':
    main()
