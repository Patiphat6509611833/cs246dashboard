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
        fig4 = px.bar(mcanteen.value_counts(), x=mcanteen.value_counts().index, y=mcanteen.value_counts().values, labels={'y': 'จำนวน'})
        st.plotly_chart(fig4)
        # แยกและทำความสะอาดข้อมูล
        eating_times = df['ในหนึ่งวันท่านรับประทานอาหารในช่วงเวลาไหนบ้าง'].str.split(',').explode().str.strip()

# นับความถี่ของแต่ละค่า
        eating_times_count = eating_times.value_counts()

# สร้าง DataFrame จากค่าที่นับได้
        eating_times_df = pd.DataFrame({'time': eating_times_count.index, 'count': eating_times_count.values})

# เรียงข้อมูลตามช่วงเวลา
        eating_times_df = eating_times_df.sort_values(by='time')

# สร้างกราฟเส้น
        fig_line = px.line(eating_times_df, x='time', y='count', title='จำนวนคนที่รับประทานอาหารในแต่ละช่วงเวลา', markers=True)

# เรียกใช้ Streamlit เพื่อแสดงผล
        st.plotly_chart(fig_line)




























