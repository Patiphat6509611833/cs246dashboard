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


# สร้าง sidebar
with st.sidebar:
    st.title(' US Population Dashboard')
    
    # สร้างรายการชั้นปีที่กำลังศึกษาอยู่
    grade_list = list(df['ชั้นปีที่กำลังศึกษาอยู่'].unique())[::-1]
    
    # เลือกชั้นปี
    selected_grade = st.selectbox('Select a grade', grade_list)
    
    # กรองข้อมูลตามชั้นปีที่เลือก
    df_selected_grade = df[df['ชั้นปีที่กำลังศึกษาอยู่'] == selected_grade]
    
    #

    # สร้างรายการธีมสี
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    
    # เลือกธีมสี
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

fig = px.pie(df, names='โปรดระบุเพศ')

# เรียกใช้ Streamlit เพื่อแสดงผล
st.plotly_chart(fig)