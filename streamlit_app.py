#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

#######################
# Page configuration
st.set_page_config(
    page_title="cs246 DASHBOARD",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")


#######################
# Load data
df = pd.read_csv('data/แบบสอบถามพฤติกรรมการเลือกซื้ออาหารของนักศึกษามหาวิทยาลัยธรรมศาสตร์  (Responses) - Form Responses 1.csv')


#######################
# Sidebar



fig = px.pie(df, names='โปรดระบุเพศ')

# เรียกใช้ Streamlit เพื่อแสดงผล
st.plotly_chart(fig)


fig3 = px.bar(df, y='ท่านพักอยู่ที่ใด')

# เรียกใช้ Streamlit เพื่อแสดงผล
st.plotly_chart(fig3)

mcanteen = df['โรงอาหารที่ท่านใช้บริการเป็นประจำ'].str.split(',').explode().str.strip()

# สร้างกราฟแท่ง
fig4 = px.bar(mcanteen.value_counts(), x=mcanteen.value_counts().index, y=mcanteen.value_counts().values, labels={'y': 'จำนวน'})

# เรียกใช้ Streamlit เพื่อแสดงผล
st.plotly_chart(fig4)