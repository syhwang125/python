import pandas as pd

# 각 모델의 성능 결과 수동 입력 (예시)
performance_comparison = pd.DataFrame({
    "Model": ["Logistic Regression", "Optimized Random Forest"],
    "Accuracy": [0.96, 0.97],     # 예시 값
    "Precision": [0.18, 0.26],    # class 1 (이상)
    "Recall": [0.12, 0.64],
    "F1-score": [0.14, 0.37]
})

print(performance_comparison)
# 모델 성능 비교
# Logistic Regression vs Optimized Random Forest
