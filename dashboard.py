import streamlit as st
import pandas as pd
import numpy as np
import firebase_admin
from firebase_admin import credentials, db
import time
from datetime import datetime
import plotly.express as px

# --- Must be first ---
st.set_page_config(
    page_title="IoT Heart Disease Monitor",
    layout="wide",
    page_icon="❤️"
)


# Firebase setup
cred = credentials.Certificate(r"C:\Users\aksha\OneDrive\Documents\iot health\iot-virtualhealth-firebase-adminsdk-fbsvc-189cd6f0b0.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://iot-virtualhealth-default-rtdb.firebaseio.com/"
})
ref = db.reference("/patients")


# --- Streamlit page header ---
st.markdown("<h1 style='text-align: center; color: red;'>❤️ IoT Heart Disease Monitor</h1>", unsafe_allow_html=True)
st.markdown("### Real-time monitoring of patient vitals and risk prediction", unsafe_allow_html=True)

# --- Placeholder for live update ---
placeholder = st.empty()

def load_data(limit=20):
    data = ref.order_by_key().limit_to_last(limit).get()
    if data:
        df = pd.DataFrame(list(data.values()))
        numeric_cols = ['age', 'trestbps', 'chol', 'thalach']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        df.dropna(inplace=True)
        return df
    else:
        return pd.DataFrame()

# --- Live dashboard ---
while True:
    df = load_data()
    if df.empty:
        st.warning("No data yet. Is the simulator running?")
        time.sleep(5)
        continue

    with placeholder.container():
        latest = df.iloc[-1]

        # --- Latest Vitals in 4 metric cards ---
        st.subheader("Latest Vitals")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Age", latest['age'])
        col2.metric("Blood Pressure", f"{latest['trestbps']} mmHg")
        col3.metric("Cholesterol", f"{latest['chol']} mg/dl")
        col4.metric("Heart Rate", f"{latest['thalach']} bpm")

        # --- Prediction with color ---
        pred_color = "green" if latest['prediction'] == "Normal" else "red"
        st.markdown(f"### Prediction: <span style='color:{pred_color}'>{latest['prediction']}</span>", unsafe_allow_html=True)

        # --- Add explainability: simple feature contribution ---
        st.subheader("Prediction Insight")
        st.markdown(
            f"""
            - Blood Pressure: {latest['trestbps']} mmHg  
            - Cholesterol: {latest['chol']} mg/dl  
            - Heart Rate: {latest['thalach']} bpm  
            
            ⚠️ The model predicts **At Risk** if BP, cholesterol, or heart rate is high.  
            🟢 Lower values indicate **Normal** status.
            """,
            unsafe_allow_html=True
        )

        # --- Last 5 records ---
        st.subheader("Last 5 Records")
        st.dataframe(df[['age','trestbps','chol','thalach','prediction','timestamp']].tail(5))

        # --- Vitals over time charts ---
        st.subheader("Vitals Over Time (Last 20 Records)")
        chart_data = df[['trestbps','chol','thalach','timestamp']].tail(20)
        chart_data.set_index('timestamp', inplace=True)
        fig = px.line(chart_data, labels={'value':'Value','timestamp':'Time'}, title="Vitals Trend")
        st.plotly_chart(fig, use_container_width=True)

    # Refresh every 5 seconds
    time.sleep(5)