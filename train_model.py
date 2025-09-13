import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, accuracy_score
import joblib
import numpy as np

# Load data
data = pd.read_csv(r'C:\Users\aksha\OneDrive\Documents\iot health\processed.cleveland.data.csv', na_values='?')
data.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# Handle missing values
data.replace('?', np.nan, inplace=True)
for col in ['ca', 'thal']:
    data[col] = data[col].astype(float)
data.fillna(data.median(), inplace=True)

# Convert target: 0 = Normal, 1 = At Risk
data['target'] = data['target'].apply(lambda x: 0 if x == 0 else 1)

# Features and target
X = data.drop('target', axis=1)
y = data['target']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest (avoid overfitting with max_depth)
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)

# Evaluate
y_pred = rf.predict(X_test)
print("✅ Test Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 5-Fold CV
cv_scores = cross_val_score(rf, X, y, cv=5)
print("✅ 5-Fold CV Accuracy:", cv_scores.mean())

# Save model
joblib.dump(rf, "model/heart_rf_model.pkl")
print("🎯 Model saved as heart_rf_model.pkl")