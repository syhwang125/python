import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 피처 이름 생성
num_features = ['Torque [Nm]', 'Tool wear [min]', 'Process temperature [K]']
cat_features = ['Type_H', 'Type_L']  # OneHotEncoding 후 예상 출력

all_features = num_features + cat_features

# 피처 중요도 가져오기
importances = best_model.named_steps["classifier"].feature_importances_
importance_df = pd.DataFrame({
    "Feature": all_features,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

# 시각화
plt.figure(figsize=(8, 5))
sns.barplot(x="Importance", y="Feature", data=importance_df, palette="Blues_d")
plt.title("🔍 Feature Importance (Random Forest)")
plt.tight_layout()
plt.show()
