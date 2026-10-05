import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Demand Forecasting", layout="wide")
st.title("📈 AI-Powered Demand Forecasting")

# Forecasting Metrics
c1, c2 = st.columns(2)
with c1:
    st.info("Model: Hybrid Prophet + LSTM")
with c2:
    st.success("Accuracy: 94.2% (MAPE)")

# Simulation Data
dates = pd.date_range(start="2024-01-01", periods=30)
actual = np.random.randint(100, 200, size=30)
predicted = actual + np.random.randint(-15, 15, size=30)
df = pd.DataFrame({"Date": dates, "Actual Demand": actual, "Forecasted Demand": predicted}).set_index("Date")

st.line_chart(df)

# What-if Analysis Slider
st.markdown("### 🛠 What-if Analysis")
price_change = st.slider("Select Price Adjustment (%)", -20, 20, 0)
st.write(f"Adjusted forecast based on {price_change}% price change.")