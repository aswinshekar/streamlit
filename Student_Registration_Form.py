import streamlit as st
from datetime import date
st.title("STUDENT REGISTRATION FORM")
name=st.text_input("ENTER YOUR NAME")
age=st.number_input("ENTER AGE",min_value=0)
date=st.date_input("ENTER DOB",min_value=date(1990,1,1),
                   max_value=date.today(),
                   value=date(2026,1,1))
email=st.text_input("ENTER EMAIL")
gender=st.radio("SELECT GENDER",["Female",'Male'])
course=st.selectbox("SELECT COURSE",["PYTHON","JAVA","DOTNET","TESTING"])

btn=st.button("REGISTER")
if btn:
    st.write("STUDENT DETAILS DETAILS")
    st.write("NAME",name)
    st.write("AGE",age)
    st.write("DATE",date)
    st.write("EMAIL",email)
    st.write("GENDER",gender)
    st.write("COURSE",course)