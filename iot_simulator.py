import pandas as pd
import time
import firebase_admin
from firebase_admin import credentials, db
import joblib
from datetime import datetime
import numpy as np

# Load model
model = joblib.load("model/heart_rf_model.pkl")

# Load data
data = pd.read_csv(r"C:\Users\aksha\OneDrive\Documents\iot health\processed.cleveland.data.csv", header=None)
data.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# --- Preprocess ---
data.replace('?', np.nan, inplace=True)
for col in ['ca', 'thal']:
    data[col] = data[col].astype(float)
data.fillna(data.median(), inplace=True)


# Firebase setup
cred = credentials.Certificate(r"C:\Users\aksha\OneDrive\Documents\iot health\iot-virtualhealth-firebase-adminsdk-fbsvc-189cd6f0b0.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://iot-virtualhealth-default-rtdb.firebaseio.com/"
})
ref = db.reference("/patients")

# Simulator loop
while True:
    patient = data.sample(1).iloc[0].copy()

    # Ensure numeric
    features = patient.drop(['target']).astype(float).values.reshape(1, -1)
    pred = model.predict(features)[0]
    pred_label = "Normal" if pred == 0 else "At Risk"

    # Prepare record
    record = patient.drop(['target']).to_dict()
    record = {k: float(v) for k, v in record.items()}  # ensure numeric
    record['prediction'] = pred_label
    record['timestamp'] = datetime.now().isoformat()

    # Upload to Firebase
    ref.push(record)
    print("Uploaded:", record)
    time.sleep(5)