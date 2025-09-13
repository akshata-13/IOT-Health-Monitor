# ❤️ IoT Heart Disease Monitoring System

## 📌 Overview
This project is an **IoT-based health monitoring system** that:
- Simulates patient health data (age, blood pressure, cholesterol, heart rate).
- Uploads it to **Firebase Realtime Database** (IoT data layer).
- Uses a **Random Forest ML model** to classify patients as:
  - ✅ Normal
  - ⚠️ At Risk
- Displays live vitals and predictions on a **Streamlit dashboard**.

---

## 🏗️ Project Architecture
1. **Data Source** → Cleveland Heart Disease dataset.
2. **ML Model** → Random Forest trained on patient vitals.
3. **IoT Simulator** → Pushes patient data every 5s to Firebase.
4. **Dashboard** → Displays vitals, predictions, and live charts.

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/akshata-13/IOT-Heart-Monitor
cd IOT-Heart-Monitor

---

2️⃣ **Create Environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣** Install Dependencies**
```bash
pip install -r requirements.txt

4️⃣ **Firebase Setup**
```bash
Create Firebase project with Realtime Database.
Download your serviceAccountKey.json.
Place it inside /firebase/ (this file is not uploaded to GitHub).

5️⃣** Train Model**
```bash
python train_model.py

6️⃣ **Run IoT Simulator**
```bash
python simulator/iot_simulator.py

7️⃣ **Run Dashboard**
```bash
streamlit run dashboard/dashboard.py
