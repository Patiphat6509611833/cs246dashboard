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

fig2 = px.pie(df, names='ท่านกำลังศึกษาอยู่คณะใด')

# เรียกใช้ Streamlit เพื่อแสดงผล
st.plotly_chart(fig2)