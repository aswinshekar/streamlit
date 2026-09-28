import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.info("ADD NEW BOOK RECORD")

title=st.text_input("ENTER TITLE:")
author=st.text_input("ENTER AUTHOR NAME")
price=st.number_input("ENTER PRICE",min_value=0)
page=st.number_input("ENTER THE NO.OF PAGES",min_value=0)
language=st.text_input("ENTER LANGUAGE")

btn=st.button("ADD")

if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(title,author,price,page,language)
    st.success("RECORD ADDED SUCCESSFULLY")