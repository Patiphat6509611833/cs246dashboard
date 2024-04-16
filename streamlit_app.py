#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import seaborn as sns

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



heatmap_data = df['ในหนึ่งวันท่านรับประทานอาหารในช่วงเวลาไหนบ้าง'].str.get_dummies(sep=', ')
heatmap = sns.heatmap(heatmap_data.groupby(heatmap_data.columns.tolist()).size().unstack(), annot=True, cmap="YlGnBu")




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
    st.pyplot(heatmap.figure)
