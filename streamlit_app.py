import streamlit as st

"""
# Welcome to Financial Calculator!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

"""

numone = st.text_input("Number One", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None,  placeholder=None, disabled=False, label_visibility="visible");
numtwo = st.text_input("Number Two", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible");

btn = st.button("Add")
if btn:
    addition = int(numone) + int(numtwo);
    st.write("Addition of Num 1 and Num 2", addition)
else:
    st.write("Enter Two values and click Add Button")
