import streamlit as st
import pandas as pd

st.set_page_config(page_title="Executive Summary", layout="wide")

st.title("📊 RetailPulse: Executive Summary")
st.markdown("---")

# Display key metrics using columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Sales", value="$45,23,000", delta="+12% from last month")

with col2:
    st.metric(label="Active Customers", value="1,420", delta="+5.4%")

with col3:
    st.metric(label="Total Orders", value="8,540", delta="-1.2%")

st.markdown("### 📈 Overview")
st.write("""
This page displays the high-level executive summary of your retail analytics project. 
From here, you can get a quick snapshot of the overall business performance.
""")

# Fixed and ordered chart data
chart_data = pd.DataFrame({
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Sales': [12000, 15000, 14000, 18000, 22000, 30000, 28000]
})

chart_data['Day'] = pd.Categorical(
    chart_data['Day'], 
    categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 
    ordered=True
)

chart_data = chart_data.sort_values('Day')

st.line_chart(chart_data.set_index('Day'))