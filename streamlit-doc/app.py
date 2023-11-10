import streamlit as st
from utils.login import check_password

if not check_password():
    st.stop()

st.write("SUCCESS - Login")