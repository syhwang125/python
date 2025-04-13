import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


#### 예측 모델 코드 (로지스틱 회귀) 

# 데이터 불러오기
# kaggle data https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020
df = pd.read_csv('ai4i2020.csv')

# 주요 피처 및 타겟 설정
features = ['Torque [Nm]', 'Tool wear [min]', 'Process temperature [K]', 'Type']
target = 'Machine failure'
X = df[features]
y = df[target]

# 전처리 설정
numeric_features = ['Torque [Nm]', 'Tool wear [min]', 'Process temperature [K]']
categorical_features = ['Type']

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(drop='first'), categorical_features)
])

# 파이프라인 구성
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])

# 학습/테스트 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)

# 학습
pipeline.fit(X_train, y_train)

# 예측 및 평가
y_pred = pipeline.predict(X_test)
print(" Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\n Classification Report:")
print(classification_report(y_test, y_pred, digits=4))
