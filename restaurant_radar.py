import pygal
radar_chart = pygal.Radar()
radar_chart.title = '餐厅评分数据'
radar_chart.x_labels = ['味道', '卫生', '服务', '价格', '环境']
radar_chart.add('老王炸鸡', [9, 6, 6, 4, 7])
radar_chart.add('小明快餐', [7, 8, 9, 6, 8])
radar_chart.add('阿强烧烤', [10, 4, 6, 8, 4])
radar_chart.add('萌仔汉堡', [7, 6, 5, 4, 6])
radar_chart.render_in_browser()