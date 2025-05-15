import streamlit as st
import pandas as pd

# 设置页面标题
st.set_page_config(page_title="TP-Link Nordic GTM Tool", layout="wide")

# 页面主标题
st.title("TP-Link Nordic GTM Tool")

# 示例项目数据（你可以在这里替换成实际数据）
data = [
    {"Project": "Weekly Sell-out Tracker", "URL": "https://example.com/sellout"},
    {"Project": "Inventory Dashboard", "URL": "https://example.com/inventory"},
    {"Project": "Price Monitoring", "URL": "https://example.com/pricing"},
]

# 转换为 DataFrame 并格式化 URL
df = pd.DataFrame(data)
df["URL"] = df["URL"].apply(lambda x: f"[Link]({x})")

# 显示表格
st.table(df)
