# ❤️ IoT Heart Disease Monitoring System

## 📌 Overview

This project is an **IoT-based health monitoring system** that:

* 📡 **Simulates patient health data** (age, blood pressure, cholesterol, heart rate).
* ☁️ **Uploads it to Firebase Realtime Database** (IoT data layer).
* 🤖 **Uses a Random Forest ML model** to classify patients as:

  * ✅ **Normal**
  * ⚠️ **At Risk**
* 🖥️ **Displays live vitals and predictions on a Streamlit dashboard**.

---

## 🏗️ Project Architecture

* **Data Source** → Cleveland Heart Disease dataset.
* **ML Model** → Random Forest trained on patient vitals.
* **IoT Simulator** → Pushes patient data every 5 seconds to Firebase.
* **Dashboard** → Displays vitals, predictions, and live charts.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/akshata-13/IOT-Heart-Monitor)
cd IOT-Heart-Monitor
```

### 2️⃣ Create Virtual Environment

**Linux/Mac**

```bash
python -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Firebase Setup

* Create a **Firebase project** with Realtime Database.
* Download your **`serviceAccountKey.json`**.
* Place it inside the `/firebase/` folder.

### 5️⃣ Train Model

```bash
python train_model.py
```

### 6️⃣ Run IoT Simulator

```bash
python iot_simulator.py
```

### 7️⃣ Run Dashboard

```bash
streamlit run dashboard.py
```

---

## 📊 Dashboard Features

✔️ **Latest vitals** displayed in cards.

✔️ **Color-coded prediction** (Green = Normal, Red = At Risk).

✔️ **Last 5 records table**.

✔️ **Live charts** for BP, Cholesterol, and Heart Rate.

✔️ **Explainability insights** (feature impact).

---

## 🔗 IoT Workflow

**Sensor Data (Simulated)** ➝ **Firebase Cloud** ➝ **ML Prediction** ➝ **Streamlit Dashboard**
