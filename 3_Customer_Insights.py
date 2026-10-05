import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Insights", layout="wide")
st.title("👥 Customer Segmentation & Churn Risk")

tab1, tab2 = st.tabs(["Segmentation", "Churn Risk"])

with tab1:
    st.subheader("Customer Clusters (RFM)")
    # Sample Table
    df_clusters = pd.DataFrame({
        "Segment": ["Champions", "Loyal", "At Risk", "Hibernating"],
        "Count": [150, 420, 85, 200],
        "Avg Spend": ["$1200", "$850", "$300", "$50"]
    })
    st.table(df_clusters)

with tab2:
    st.subheader("High Churn Risk Alerts")
    st.error("15 High-Value customers are at 80%+ churn risk.")
    st.button("Generate Retention Email Campaign")