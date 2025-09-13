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
