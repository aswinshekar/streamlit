import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("Read a Specific Book Record")

id = st.number_input("Book ID",min_value=0)
btn = st.button("Retrieve")

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    record = b.retrieve(id)
    print(record)
    if record:
        st.table(record)
    else:
        st.write("NO RECORDS FOUND")
