import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.header("DELETE BOOK RECORD")
id=st.number_input("Enter Book ID:")
btn=st.button("Delete record")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    status=b.delete(id)
    if status:
        st.success("Record Deleted Successfully")
    else:
        st.error("Record not Found")