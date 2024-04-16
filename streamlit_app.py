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



# กำหนดหัวข้อใน sidebar
with st.sidebar:
    st.title('🏂 US Population Dashboard')
    option = st.selectbox('เลือกหัวข้อ:', ["โรงอาหาร", "ร้านค้าภายนอก", "ทำอาหารกินเอง"])

# Load data
df = pd.read_csv('data/แบบสอบถามพฤติกรรมการเลือกซื้ออาหารของนักศึกษามหาวิทยาลัยธรรมศาสตร์  (Responses) - Form Responses 1.csv')

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("จำนวนนักศึกษาที่ตอบแบบสอบถาม:")
    st.subheader("101 คน")

st.markdown("""---""")








# กำหนดเงื่อนไขเพื่อแสดงกราฟตามหัวข้อที่เลือก
if option == "โรงอาหาร":
    col1, col2 = st.columns(2)
    with col1:

        st.header('')
        fig = px.pie(df, names='โดยปกติแล้วท่านซื้ออาหารจากโรงอาหารหรือไม่')
        st.plotly_chart(fig)
       
        st.header('')
        factors = df['ปัจจัยที่ท่านใช้ในการเลือกซื้ออาหารในโรงอาหารมหาวิทยาลัย'].str.split(',').explode().str.strip()
        top_factors = factors.value_counts().head(5)
        fig2 = px.bar(top_factors, x=top_factors.values, y=top_factors.index, orientation='h', labels={ 'y': 'ปัจจัย'})

        st.plotly_chart(fig2) 



    with col2:
        st.header('โรงอาหารที่นักศึกษามักใช้บริการ')
        mcanteen = df['โรงอาหารที่ท่านใช้บริการเป็นประจำ'].str.split(',').explode().str.strip()
        fig4 = px.bar(mcanteen.value_counts(),  y=mcanteen.value_counts().values, labels={'y': 'จำนวน'})
        st.plotly_chart(fig4)
        
























