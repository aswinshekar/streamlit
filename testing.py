import streamlit as st

# -----------------------------
# TEXT DISPLAY
# -----------------------------

st.title("My First Streamlit App")

st.header("Student Information")

st.subheader("Enter Your Details")

st.text("Welcome to my Streamlit application!")

st.write("This application is created using Python and Streamlit.")

st.markdown("**Fill in the details below:**")


# -----------------------------
# TEXT INPUT
# -----------------------------

name = st.text_input("Enter your name")


# -----------------------------
# NUMBER INPUT
# -----------------------------

age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100
)


# -----------------------------
# CHECKBOX
# -----------------------------

agree = st.checkbox("I agree to the terms")


# -----------------------------
# RADIO BUTTON
# -----------------------------

gender = st.radio(
    "Select your gender",
    ["Male", "Female", "Other"]
)


# -----------------------------
# SELECT BOX
# -----------------------------

course = st.selectbox(
    "Select your course",
    ["Python", "Java", "C++", "AI", "Data Science"]
)


# -----------------------------
# SLIDER
# -----------------------------

experience = st.slider(
    "Select your Python experience (years)",
    0,
    10
)


# -----------------------------
# BUTTON
# -----------------------------

if st.button("Submit"):

    st.write("### Student Details")

    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Course:", course)
    st.write("Python Experience:", experience, "years")

    if agree:
        st.write("You agreed to the terms.")
    else:
        st.write("You did not agree to the terms.")