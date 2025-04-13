import pandas as pd
from scipy.stats import chi2_contingency

# 데이터 불러오기
df = pd.read_csv("ai4i2020.csv")

# 교차표 생성
contingency_table = pd.crosstab(df['Type'], df['Machine failure'])

# 카이제곱 검정
chi2, p, dof, expected = chi2_contingency(contingency_table)

print("Chi-squared Test Statistic:", chi2)
print("p-value:", p)
print("Degrees of Freedom:", dof)
print("Expected Frequencies Table:\n", expected)
