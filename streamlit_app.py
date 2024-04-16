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
    st.title('โปรดเลือกหัวข้อ')
    option = st.selectbox('', ["โรงอาหาร", "ร้านค้าภายนอก", "ทำอาหารกินเอง"])

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

        st.header('เปอร์เซ็นการใช้งานโรงอาหารของนักศึกษา')
        fig = px.pie(df, names='โดยปกติแล้วท่านซื้ออาหารจากโรงอาหารหรือไม่')
        st.plotly_chart(fig)
       
        st.header('5 ปัจจัยที่ส่งผลมากที่สุดต่อการใช้บริการโรงอาหาร')
        factors = df['ปัจจัยที่ท่านใช้ในการเลือกซื้ออาหารในโรงอาหารมหาวิทยาลัย'].str.split(',').explode().str.strip()
        top_factors = factors.value_counts().head(5)
        fig2 = px.bar(top_factors, x=top_factors.values, y=top_factors.index, orientation='h', labels={ 'x': '','y': 'ปัจจัย'})

        st.plotly_chart(fig2) 

        st.header('จำนวนมื้ออาหารทีนักศึกษาใช้บริการโรงอาหารมหาวิทยาลัย')
        meal_frequency = df['โดยเฉลี่ยแล้วท่านอยู่ในมหาวิทยาลัยท่านรับประทานอาหารที่โรงอาหารวันละกี่มื้อ'].value_counts()
        fig_pie = px.pie(meal_frequency, values=meal_frequency.values, names=meal_frequency.index, title='โดยเฉลี่ยแล้วท่านซื้อ/สั่งอาหารวันละกี่มื้อ')
        st.plotly_chart(fig_pie)



    with col2:
        st.header('โรงอาหารที่นักศึกษามักใช้บริการ')
        mcanteen = df['โรงอาหารที่ท่านใช้บริการเป็นประจำ'].str.split(',').explode().str.strip()
        fig4 = px.bar(mcanteen.value_counts(), x=mcanteen.value_counts().index, y=mcanteen.value_counts().values, labels={'x': '','y': 'จำนวน'})
        st.plotly_chart(fig4)
        st.header('ช่วงเวลาที่นักศึกษามักใช้บริการโรงอาหาร')
        eating_times = df['ในหนึ่งวันท่านรับประทานอาหารในช่วงเวลาไหนบ้าง'].str.split(',').explode().str.strip()
        eating_times_count = eating_times.value_counts()
        eating_times_df = pd.DataFrame({'time': eating_times_count.index, 'count': eating_times_count.values})
        eating_times_df = eating_times_df.sort_values(by='time')
        fig_line = px.line(eating_times_df, x='time', y='count',  markers=True)
        st.plotly_chart(fig_line)


if option == "ร้านค้าภายนอก":
    col3, col4 = st.columns(2)
    with col3:

        st.header('เปอร์เซ็นการใช้งานร้านอาหารนอกมหาวิทยาลัยของนักศึกษา')
        fig5 = px.pie(df, names='โดยปกติแล้วท่านซื้อ/สั่งอาหารจากร้านค้าภายนอกหรือไม่')
        st.plotly_chart(fig5)
       
        st.header('5 ปัจจัยที่ส่งผลมากที่สุดต่อการใช้บริการนอกมหาวิทยาลัย')
        factors = df['ปัจจัยที่ท่านใช้ในการเลือกซื้ออาหารที่ร้านอาหารนอกมหาวิทยาลัย'].str.split(',').explode().str.strip()
        top_factors = factors.value_counts().head(5)
        fig6 = px.bar(top_factors, x=top_factors.values, y=top_factors.index, orientation='h', labels={ 'x': '','y': 'ปัจจัย'})

        st.plotly_chart(fig6) 
    with col4:
        st.header('จำนวนมื้ออาหารทีนักศึกษาใช้บริการร้านอาหารนอกมหาวิทยาลัย')
        meal_frequency = df['โดยเฉลี่ยแล้วท่านซื้อ/สั่งอาหารวันละกี่มื้อ'].value_counts()
        fig_pie = px.pie(meal_frequency, values=meal_frequency.values, names=meal_frequency.index, title='โดยเฉลี่ยแล้วท่านซื้อ/สั่งอาหารวันละกี่มื้อ')
        st.plotly_chart(fig_pie)

        st.header('ช่วงเวลาที่นักศึกษามักใช้บริการร้านอาหารนอกมหาวิทยาลัย')
        eating_times2 = df['ท่านซื้อ/สั่งอาหารในช่วงเวลาใดบ้าง'].str.split(',').explode().str.strip()
        eating_times_count2 = eating_times2.value_counts()
        eating_times_df2 = pd.DataFrame({'time': eating_times_count2.index, 'count': eating_times_count2.values})
        eating_times_df2 = eating_times_df2.sort_values(by='time')
        fig_line2 = px.line(eating_times_df2, x='time', y='count',  markers=True)
        st.plotly_chart(fig_line2)



if option == "ทำอาหารกินเอง":
    col5, col6 = st.columns(2)
    with col5:

        st.header('เปอร์เซ็นการทำอาหารกินเองของนักศึกษา')
        fig7= px.pie(df, names='โดยปกติแล้วท่านทำอาหารกินเองหรือไม่')
        st.plotly_chart(fig7)
        st.header('ช่วงเวลาที่นักศึกษามักใช้จะทำอาหารกินเอง')
        eating_times3 = df['ท่านทำอาหารกินเองในช่วงเวลาใดบ้าง'].str.split(',').explode().str.strip()


        eating_times_count3 = eating_times3.value_counts()


        eating_times_df3 = pd.DataFrame({'time': eating_times_count3.index, 'count': eating_times_count3.values})


        eating_times_df3 = eating_times_df3.sort_values(by='time')


        fig_line3 = px.line(eating_times_df3, x='time', y='count',  markers=True)


        st.plotly_chart(fig_line3)
        
    with col6:
        st.header('จำนวนมื้ออาหารที่นักศึกษาทำกินเอง')
        # นับความถี่ของค่าแต่ละค่าในคอลัมน์
        meal_frequency2 = df['โดยเฉลี่ยแล้วท่านทำอาหารกินเองวันละกี่มื้อ'].value_counts()

        fig_pie = px.pie(meal_frequency2, values=meal_frequency2.values, names=meal_frequency2.index, title='')


        st.plotly_chart(fig_pie)
       
       
























