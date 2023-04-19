import streamlit as st
import numpy as np
@st.cache
def largest_num(a, b, c):
    return np.max([a, b, c])

def app():
    st.title("Find the Largest Number")
    st.write("Enter three numbers and I will tell you which one is the largest.")

    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")

    if st.button("Find the largest"):
        result = largest_num(a, b, c)
        st.success(f"The largest number is {result}")
