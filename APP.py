import streamlit as st
import pandas as pd

# ✅ 这必须是第一个 Streamlit 调用
st.set_page_config(page_title="TP-Link Nordic GTM Tool", layout="wide")

# 设置背景
def set_background_image(url):
    st.markdown(
        f"""
        <style>
        html, body {{
            height: 100%;
            margin: 0;
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .stApp {{
            background-color: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 12px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 应用背景
set_background_image("https://images.unsplash.com/photo-1503264116251-35a269479413?auto=format&fit=crop&w=1950&q=80")

# 页面主标题
st.title("TP-Link Nordic GTM Tool")

# 示例项目数据（你可以在这里替换成实际数据）
data = [
    {"Project": "New product Image", "URL": "https://docs.google.com/spreadsheets/d/1pI3Fd9vRP4hqwqSKaC8A_NewI9tDiD9zQuVP0OjhqEk/edit?usp=sharing"},
    {"Project": "Elkjop Price Lookup", "URL": "https://elkjoplookup.streamlit.app/"},
    {"Project": "Elkjop Price Download", "URL": "https://elkjopdownload.streamlit.app/"},
]

# 转换为 DataFrame 并格式化 URL
df = pd.DataFrame(data)
df["URL"] = df["URL"].apply(lambda x: f"[Link]({x})")

# 显示表格
st.table(df)
