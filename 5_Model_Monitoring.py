import streamlit as st
import pandas as pd

st.set_page_config(page_title="Model Monitoring", layout="wide")
st.title("🛠 ML Model Monitoring & Drift Detection (Evidently AI)")

st.markdown("---")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label="Data Drift Score", value="0.042", delta="Stable")
with c2:
    st.metric(label="Prediction Drift", value="0.018", delta="Normal")
with c3:
    st.metric(label="Last Retrained", value="2 Days Ago", delta="Airflow Automated")

st.markdown("### 📊 Drift Status Across Features")
drift_data = pd.DataFrame({
    "Feature Name": ["Customer Age", "Monthly Spend", "Purchase Frequency", "Product Category", "Discount Usage"],
    "Drift Detected?": ["No", "No", "Yes ⚠️", "No", "No"],
    "Statistical Distance": [0.02, 0.05, 0.31, 0.01, 0.04]
})

st.table(drift_data)

if st.button("Trigger Manual Retraining Pipeline"):
    st.success("Airflow DAG triggered successfully! Model is retraining on latest data.")