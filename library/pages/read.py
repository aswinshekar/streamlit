import streamlit as st
st.title("READ ALL RECORD")
from library_db import BookListCreateRetrieveUpdateDelete
b=BookListCreateRetrieveUpdateDelete()
record=b.list()
if record:
    st.table(record)
else:
    st.write("NO RECORDS FOUND")

