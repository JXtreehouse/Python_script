# https://github.com/JackieMium/my_blog/issues/25
# https://www.zhihu.com/question/594346888
# https://bbs.huaweicloud.com/blogs/368659
# https://www.heywhale.com/mw/project/5d9fe977037db3002d4159b4
import psycopg2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import getpass
from IPython.display import HTML, display
import matplotlib.dates as dates
import matplotlib.lines as mlines

plt.style.use("ggplot")

schema_name = 'mimiciv'
# 连接到MIMIC-IV数据库
conn = psycopg2.connect(dbname='mimiciv', user='postgres', password='mimic',
                        host='10.234.211.51', port=5432)
query_schema = 'SET search_path to ' + schema_name + ';'
# 设置查询语句
# 我们选择从mimiciv_hosp.admissions表中提取hadm_id等于10006的行。
# 在写sql代码时，最好先执行“set search_path to mimiciv" 随后的所有操作均不需要指明表格的位置；否则，任何操作都应该在表格名前面加前缀mimiciv
query = query_schema + 'SELECT * FROM mimiciv_hosp.admissions WHERE hadm_id = 24065018;'

# 执行查询语句
cur = conn.cursor()
print("Successful!\n")
cur.execute(query)

# 获取结果
results = cur.fetchall()
print(results)

# 打印结果
for row in results:
    print(row)

# 关闭连接
cur.close()
conn.close()
