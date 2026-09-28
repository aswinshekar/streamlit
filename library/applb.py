# import streamlit as st
# st.title("welcome to my library app")

#WITH TAB VIEW
import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','VIEW','RETRIEVE','DELETE','UPDATE'])
b=BookListCreateRetrieveUpdateDelete()

with tab1:
    # st.title("ADD")
    st.header("ADD NEW BOOK RECORD")
    title = st.text_input("Enter book Title:")
    author = st.text_input("Author Name:")
    price = st.number_input("Price:")
    pages = st.number_input("No. of Pages:")
    language = st.text_input("Language:")
    btn = st.button("ADD BOOK")
    if btn:
        b = BookListCreateRetrieveUpdateDelete()
        b.create(title, author, price, pages, language)
        st.success("RECORD CREATED SUCCESSFULLY")

with tab2:
    # st.title("VIEW")
    st.header("READ ALL BOOK RECORD")
    b = BookListCreateRetrieveUpdateDelete()
    records = b.list()
    print("Hello")
    print(records)
    st.table(records)

with tab3:
    st.header("READ A SPECIFIC BOOK RECORD")
    id = st.number_input("Enter Book ID:")
    btn = st.button("Retrieve")
    if btn:
        b = BookListCreateRetrieveUpdateDelete()
        record = b.retrieve(id)
        print(record)
        if record:
            # st.write("Title:", record[1])
            # st.write("Author:", record[2])
            # st.write("Price:", record[3])
            # st.write("Pages:", record[4])
            # st.write("Languages:", record[5])
            st.table(record)
        else:
            print("NO RECORDS FOUND")

with tab4:
    # st.title("DELETE")
    st.header("DELETE BOOK RECORD")
    id = st.number_input("Enter Book ID:")
    btn = st.button("Delete record")
    if btn:
        b = BookListCreateRetrieveUpdateDelete()
        status = b.delete(id)
        if status == True:
            st.success("Record Deleted Successfully")
        else:
            st.error("Record not Found")

with tab5:
    # st.title("UPDATE")
    st.header("UPDATE BOOK RECORD")
    id = st.number_input("Enter Book ID:")
    title = st.text_input("Enter Book Title:")
    author = st.text_input("Enter Author Name:")
    price = st.number_input("Price:")
    pages = st.number_input("No. of Pages:")
    language = st.text_input("Language:")
    btn = st.button("Update Book")
    if btn:
        b = BookListCreateRetrieveUpdateDelete()
        status = b.update(title, author, price, pages, language, id)
        if status:
            st.success("Update Successfully")
        else:
            st.error("No Record Found")


#              django
# read without id - get()
# create - post()
# full updation- put()
# delete- delete()