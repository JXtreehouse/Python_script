import matplotlib
# https://github.com/JackieMium/my_blog/issues/25
# https://blog.csdn.net/skyskytotop/article/details/122715037?ops_request_misc=&request_id=&biz_id=102&utm_term=mimic%20sql&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-7-122715037.142^v96^pc_search_result_base8&spm=1018.2226.3001.4187
# https://www.heywhale.com/mw/project/5d9fe977037db3002d4159b4
# https://blog.csdn.net/qq_46039856/article/details/122812228
import psycopg2
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 999)
from wordcloud import WordCloud
from ydata_profiling import ProfileReport

import matplotlib.pyplot as plt
import getpass
from IPython.display import HTML, display
import matplotlib.dates as dates
import matplotlib.lines as mlines


# plt.style.use("ggplot")


schema_name = 'mimic'
# 连接到MIMIC-IV数据库
conn = psycopg2.connect(dbname='mimiciv', user='postgres', password='mimic',
                        host='10.234.211.51', port=5432)
query_schema = 'SET search_path to ' + schema_name + ';'



# # 设置查询语句
# # 我们选择从mimiciv_hosp.admissions表中提取hadm_id等于10006的行。
# # 在写sql代码时，最好先执行“set search_path to mimiciv" 随后的所有操作均不需要指明表格的位置；否则，任何操作都应该在表格名前面加前缀mimiciv
query1 = query_schema + 'SELECT * FROM  mimiciv_hosp.admissions'

query2 = query_schema + 'SELECT * FROM mimiciv_icu.icustays'

# # 病患住院记录表数据可视化
# # 执行查询语句
a = pd.read_sql_query(query1, conn)
b = pd.read_sql_query(query2, conn)


# 关联病人住院信息数据集和病人在icu的停留时间数据集
# on: 两个数据集
merge = pd.merge(a, b, on=['subject_id','hadm_id'])

# 基于列subject_id、hadm_id进行merge
admission_type_with_icu_stay = merge.groupby(by=['admission_type']).agg({'los':'mean'}).reset_index()
print(admission_type_with_icu_stay)
x = admission_type_with_icu_stay.admission_type
y = admission_type_with_icu_stay.los

plt.figure(figsize=(6,4))
plt.bar(x,y)
plt.xlabel('Admission Type')
plt.ylabel('Average ICU Stay Length (day)')
plt.title('Average ICU Stay Length of Differenct Admission Type')
plt.show()