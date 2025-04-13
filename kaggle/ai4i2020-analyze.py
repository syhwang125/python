import pandas as pd

# 데이터 로드
df = pd.read_csv('ai4i2020.csv')

# 데이터프레임 기본 정보 출력
df_info = df.info()
df_head = df.head()
df_description = df.describe()
df_nulls = df.isnull().sum()

df.columns, df_info, df_head, df_description, df_nulls
