import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

### SMOTE(데이터 불균형해소를 위한 오버샘플링 기법) 적용 예시
### 로지스틱 회귀 모델을 사용한 예시

# 데이터 로드
df = pd.read_csv("ai4i2020.csv")

# 피처/타겟 설정
features = ['Torque [Nm]', 'Tool wear [min]', 'Process temperature [K]', 'Type']
target = 'Machine failure'
X = df[features]
y = df[target]

# 수치형/범주형 피처 정의
numeric_features = ['Torque [Nm]', 'Tool wear [min]', 'Process temperature [K]']
categorical_features = ['Type']

# 전처리 구성
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(drop='first'), categorical_features)
])

# 파이프라인: 전처리 + SMOTE + 로지스틱 회귀
pipeline = ImbPipeline(steps=[
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=42)),
    ('classifier', LogisticRegression(max_iter=1000))
])

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42)

# 모델 학습
pipeline.fit(X_train, y_train)

# 예측 및 평가
y_pred = pipeline.predict(X_test)
print("📊 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred, digits=4))
