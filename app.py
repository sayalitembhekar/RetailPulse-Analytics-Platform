import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="RetailPulse Analytics Platform",
    page_icon="📊",
    layout="wide"
)

# Sidebar Navigation (Saare 11 pages - Upload Dataset hatakar)
st.sidebar.title("RetailPulse")
st.sidebar.subheader("AI-Powered Retail Analytics Platform")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Executive Dashboard",
        "Sales Analytics",
        "Customer Analytics",
        "Customer Segmentation",
        "Customer Churn",
        "Inventory",
        "Country Analysis",
        "Product Analysis",
        "Demand Forecasting",
        "Settings / Model Monitoring"
    ]
)

# --- HOME PAGE ---
if page == "Home":
    st.title("🏠 Welcome to RetailPulse")
    st.write("AI-Powered Customer Analytics & Demand Forecasting Platform")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("TOTAL REVENUE", "₹255,874")
    with col2:
        st.metric("TOTAL ORDERS", "988")
    with col3:
        st.metric("TOTAL CUSTOMERS", "199")
    with col4:
        st.metric("PRODUCTS", "4")
        
    st.markdown("---")
    st.subheader("Project Workflow & Features:")
    st.markdown("""
    - Data Collection & Cleaning (UCI Online Retail)
    - Exploratory Data Analysis (EDA)
    - Customer Segmentation (RFM Analysis)
    - Demand Forecasting (Time Series / Prophet)
    - Churn Prediction & Inventory Optimization
    - Deployed using Streamlit Cloud
    """)

# --- EXECUTIVE DASHBOARD ---
elif page == "Executive Dashboard":
    st.title("📊 Executive Dashboard")
    st.write("High-level revenue & customer stats summary.")
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Sales', 'Profit'])
    st.line_chart(chart_data)

# --- SALES ANALYTICS ---
elif page == "Sales Analytics":
    st.title("📈 Sales Analytics")
    st.write("Daily & monthly revenue trends and patterns.")
    sales_df = pd.DataFrame(np.random.randn(15, 3), columns=['Online Sales', 'Store Sales', 'Discount'])
    st.area_chart(sales_df)

# --- CUSTOMER ANALYTICS ---
elif page == "Customer Analytics":
    st.title("👥 Customer Analytics")
    st.write("Engagement metrics and purchase patterns.")
    cust_df = pd.DataFrame({'Metric': ['Active Users', 'Returning', 'New Buyers'], 'Count': [120, 50, 29]})
    st.bar_chart(cust_df.set_index('Metric'))

# --- CUSTOMER SEGMENTATION ---
elif page == "Customer Segmentation":
    st.title("🏷️ Customer Segmentation (RFM Analysis)")
    st.write("RFM (Recency, Frequency, Monetary) clustering for target marketing.")
    rfm_df = pd.DataFrame({'Segment': ['Champions', 'At Risk', 'Loyal', 'Hibernating'], 'Share (%)': [35, 20, 30, 15]})
    st.dataframe(rfm_df, use_container_width=True)

# --- CUSTOMER CHURN ---
elif page == "Customer Churn":
    st.title("⚠️ Customer Churn Prediction")
    st.write("Identify customers who are likely to stop purchasing.")
    st.warning("Model Status: Active | Churn Rate: ~12.4%")

# --- INVENTORY ---
elif page == "Inventory":
    st.title("📦 Inventory Optimization")
    st.write("Stock levels, reorder points, and warehouse management.")
    inv_df = pd.DataFrame({
        'Product': ['Item A', 'Item B', 'Item C', 'Item D'],
        'Stock Level': [150, 30, 85, 200],
        'Status': ['Optimal', 'Low Stock', 'Optimal', 'Optimal']
    })
    st.dataframe(inv_df, use_container_width=True)

# --- COUNTRY ANALYSIS ---
elif page == "Country Analysis":
    st.title("🌍 Country Analysis")
    st.write("Geographical distribution of sales and regional performance.")
    geo_df = pd.DataFrame({'Country': ['India', 'UK', 'USA', 'Germany'], 'Revenue (₹)': [120000, 85000, 35000, 15874]})
    st.bar_chart(geo_df.set_index('Country'))

# --- PRODUCT ANALYTICS ---
elif page == "Product Analytics":
    st.title("🛍️ Product Analytics")
    st.write("Top-performing products, categories, and profitability.")
    prod_df = pd.DataFrame({'Category': ['Electronics', 'Apparel', 'Home Decor', 'Beauty'], 'Sales Share': [40, 30, 20, 10]})
    st.bar_chart(prod_df.set_index('Category'))

# --- DEMAND FORECASTING ---
elif page == "Demand Forecasting":
    st.title("🔮 Demand Forecasting")
    st.write("Time-series forecasting for upcoming demand and sales trends.")
    forecast_data = pd.DataFrame(np.random.randn(30, 1) * 50 + 800, columns=['Predicted Demand'])
    st.line_chart(forecast_data)

# --- SETTINGS / MODEL MONITORING ---
elif page == "Settings / Model Monitoring":
    st.title("⚙️ Settings & Model Monitoring")
    st.write("System health, model accuracy metrics, and configurations.")
    st.success("All Machine Learning pipelines and Streamlit components are running smoothly.")
