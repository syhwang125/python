import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
import joblib


## 최적화된 RandomForest + SMOTE 전체 코드

# 데이터 불러오기
df = pd.read_csv("ai4i2020.csv")

# 피처 및 타겟
features = ['Torque [Nm]', 'Tool wear [min]', 'Process temperature [K]', 'Type']
target = 'Machine failure'
X = df[features]
y = df[target]

# 전처리 정의
numeric_features = ['Torque [Nm]', 'Tool wear [min]', 'Process temperature [K]']
categorical_features = ['Type']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(drop='first'), categorical_features)
])

# 최적화된 모델 구성 (예: best_params_ 결과 기반)
optimized_rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=2,
    random_state=42,
    n_jobs=-1
)

# 전체 파이프라인
pipeline = ImbPipeline(steps=[
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=42)),
    ('classifier', optimized_rf)
])

# 학습/테스트 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)

# 모델 학습
pipeline.fit(X_train, y_train)

# 평가
y_pred = pipeline.predict(X_test)
print("📊 Classification Report:\n", classification_report(y_test, y_pred, digits=4))
print("🔍 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 모델 저장
joblib.dump(pipeline, "optimized_random_forest_model.pkl")
