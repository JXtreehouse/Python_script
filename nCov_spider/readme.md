- 2020 冠状病毒疫情爬虫
- 疫情数据可视化

# 技术栈
- mongodb 用于存储采集数据
- mysql 5.7 用于存储从mogodb采集的数据
- python 3.7 采集数据和转换mongodb数据到mysql

# requirements.txt
导出原项目的依赖
```bash
pip3 freeze > requirements.txt
```
在新项目中一次性安装依赖
```bash
 pip3 install -r requirements.txt
```