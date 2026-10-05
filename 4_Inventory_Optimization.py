import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inventory Optimization", layout="wide")
st.title("📦 Inventory Optimization & Stock Recommendations")

st.markdown("---")

# Metrics Overview
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Carrying Cost", value="$79,645", delta="-8.2%")
with col2:
    st.metric(label="Reorder Alerts", value="7,519", delta="+3 items")
with col3:
    st.metric(label="Safety Buffer", value="2,765", delta="Optimal")

st.markdown("### 🔍 Inventory Filters & Recommendations")
st.write("Manage stock distribution, reorder points, and category-level safety thresholds based on ML demand forecasts.")

# Sample Data Table
inventory_df = pd.DataFrame({
    "SKU ID": ["SKU-101", "SKU-102", "SKU-103", "SKU-104"],
    "Category": ["Electronics", "Apparel", "Home & Kitchen", "Groceries"],
    "Current Stock": [120, 45, 300, 15],
    "Reorder Point": [150, 60, 250, 40],
    "Action Status": ["⚠️ Reorder Soon", "🚨 Critical Stock", "✅ Optimal", "🚨 Critical Stock"]
})

st.dataframe(inventory_df, use_container_width=True, hide_index=True)