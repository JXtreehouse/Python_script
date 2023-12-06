import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

schema_name = 'mimic'
# 连接到MIMIC-IV数据库
conn = psycopg2.connect(dbname='mimiciv', user='postgres', password='mimic',
                        host='10.234.211.51', port=5432)
query_schema = 'SET search_path to ' + schema_name + ';'



# # # 设置查询语句
# # # 我们选择从mimiciv_hosp.admissions表中提取hadm_id等于10006的行。
# # # 在写sql代码时，最好先执行“set search_path to mimiciv" 随后的所有操作均不需要指明表格的位置；否则，任何操作都应该在表格名前面加前缀mimiciv
# query1 = query_schema + 'SELECT subject_id, hadm_id, admittime, dischtime, admission_type FROM  mimiciv_hosp.admissions'
#
# # 运行查询并将结果分配给变量
# admissions_pd = pd.read_sql_query(query1,conn)
# admissions_pd.head()
# print(admissions_pd.head())

query = """
SELECT de.stay_id
  , (strftime('%s',de.charttime)-strftime('%s',ie.intime))/60.0/60.0 as HOURS
  , di.label
  , de.value
  , de.valuenum
  , de.uom
FROM mimiciv_icu.chartevents de
INNER join mimiciv_icu.d_items di
ON de.itemid = di.itemid
INNER join mimiciv_icu.icustays ie
ON de.stay_id = ie.stay_id
WHERE de.stay_id = 252522
ORDER BY charttime;
"""

ce = pd.read_sql_query(query,conn)

# OPTION 2: load chartevents from a CSV file
# ce = pd.read_csv('data/example_chartevents.csv', index_col='HOURSSINCEADMISSION')
print(ce.head())


