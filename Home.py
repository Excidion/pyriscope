import streamlit as st
from content.layout import BasePage, set_sidebar_width


set_sidebar_width(400)


st.title("Periscope")
st.write("Take a look into your black box model.")
