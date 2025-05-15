import streamlit as st
import pandas as pd

# 设置页面标题和宽度
st.set_page_config(page_title="TP-Link Nordic GTM Tool", layout="wide")

# 设置背景图
def set_background_image(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 设置内容容器样式（半透明白底 + 圆角）
def set_content_container_style():
    st.markdown(
        """
        <style>
        .block-container {
            background-color: rgba(255, 255, 255, 0.88);
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# 应用背景图和样式
set_background_image("https://static.wallhaven.cc/images/layout/blue-gradients.020-wh.jpg")
set_content_container_style()

# 设置页面标题
st.set_page_config(page_title="TP-Link Nordic GTM Tool", layout="wide")

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
