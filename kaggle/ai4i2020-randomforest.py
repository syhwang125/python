import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
import joblib



import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
df = pd.read_csv("ai4i2020.csv")

# 피처 및 타겟
features = ['Torque [Nm]', 'Tool wear [min]', 'Process temperature [K]', 'Type']
target = 'Machine failure'
X = df[features]
y = df[target]

# 수치형 / 범주형 피처
numeric_features = ['Torque [Nm]', 'Tool wear [min]', 'Process temperature [K]']
categorical_features = ['Type']

# 전처리
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(drop='first'), categorical_features)
])

# 파이프라인 구성: 전처리 → SMOTE → RandomForest
pipeline = ImbPipeline(steps=[
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=42)),
    ('classifier', RandomForestClassifier(random_state=42))
])

# 하이퍼파라미터 탐색
param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [None, 10, 20],
    'classifier__min_samples_split': [2, 5]
}

# 학습/테스트 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)

# GridSearchCV 사용
grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='recall', n_jobs=-1)
grid_search.fit(X_train, y_train)

# 최적 모델로 예측
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# 결과 출력
print("✅ Best Parameters:", grid_search.best_params_)
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred, digits=4))
print("\n🔍 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 모델 저장
joblib.dump(best_model, "best_random_forest_model.pkl")


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
