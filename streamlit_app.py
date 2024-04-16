#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
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
df_reshaped = pd.read_csv('data/แบบสอบถามพฤติกรรมการเลือกซื้ออาหารของนักศึกษามหาวิทยาลัยธรรมศาสตร์  (Responses) - Form Responses 1.csv')


#######################
# Sidebar


# สร้าง sidebar
with st.sidebar:
    st.title(' US Population Dashboard')
    
    # สร้างรายการชั้นปีที่กำลังศึกษาอยู่
    grade_list = list(df_reshaped['ชั้นปีที่กำลังศึกษาอยู่'].unique())[::-1]
    
    # เลือกชั้นปี
    selected_grade = st.selectbox('Select a grade', grade_list)
    
    # กรองข้อมูลตามชั้นปีที่เลือก
    df_selected_grade = df_reshaped[df_reshaped['ชั้นปีที่กำลังศึกษาอยู่'] == selected_grade]
    
    # เรียงลำดับข้อมูลตามประชากรจากมากไปน้อย
    df_selected_grade_sorted = df_selected_grade.sort_values(by="population", ascending=False)

    # สร้างรายการธีมสี
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    
    # เลือกธีมสี
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

#######################
# Plots
# นับจำนวนข้อมูลในแต่ละกลุ่ม
count_by_year = df_reshaped['ชั้นปีที่กำลังศึกษาอยู่'].value_counts()

# สร้างกราฟวงกลม
fig, ax = plt.subplots()
ax.pie(count_by_year, labels=count_by_year.index, autopct='%1.1f%%')

# แสดงกราฟใน Streamlit
st.pyplot(fig)
