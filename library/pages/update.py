import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.header("UPDATE BOOK RECORD")
id=st.number_input("Enter Book ID:")
title=st.text_input("Enter Book Title:")
author=st.text_input("Enter Author Name:")
price=st.number_input("Price:")
page=st.number_input("No. of Pages:")
language=st.text_input("Language:")
btn=st.button("Update Book")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    status=b.update(title,author,price,page,language,id)
    if status:
        st.success("Update Successfully")
    else:
        st.error("No Record Found")
