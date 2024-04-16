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



# Load data
df = pd.read_csv('data/แบบสอบถามพฤติกรรมการเลือกซื้ออาหารของนักศึกษามหาวิทยาลัยธรรมศาสตร์  (Responses) - Form Responses 1.csv')
# เริ่มต้น Slider
selected_option = st.select_slider(
    label="เลือกหัวข้อ:",
    options=["โรงอาหาร", "ร้านค้าภายนอก", "ทำอาหารกินเอง"]
)

# แสดงผลหัวข้อที่ถูกเลือก
st.write("คุณเลือก:", selected_option)



left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("จำนวนผู้ตอบแบบสอบถาม:")
    st.subheader("101 คน")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader("")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader("  ")

st.markdown("""---""")





fig = px.pie(df, names='ท่านพักอยู่ที่ใด')








mcanteen = df['โรงอาหารที่ท่านใช้บริการเป็นประจำ'].str.split(',').explode().str.strip()
fig4 = px.bar(mcanteen.value_counts(), x=mcanteen.value_counts().index, y=mcanteen.value_counts().values, labels={'y': 'จำนวน'})





# First column: Pie chart
col1, col2 = st.columns(2)  # แบ่งหน้าจอเป็น 2 คอลัมน์

with col1:
    st.header('ที่พักของนักศึกษา')
    st.plotly_chart(fig)  # แสดง Pie chart ในคอลัมน์แรก

# Second column: Bar chart
with col2:
    
    st.header('โรงอาหารที่ได้รับความนิยม')
    st.plotly_chart(fig4)  # แสดง Bar chart ของโรงอาหารในคอลัมน์ที่สาม
    