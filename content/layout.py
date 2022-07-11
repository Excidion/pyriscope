import streamlit as st
from time import sleep

class BasePage:
    def __init__(self, title):
        self.title = title
        if st.sidebar.button(self.title):
            self.build_page()
    
    def build_page(self):
        with st.spinner(f"Preparing {self.title}..."):
            self.get_content()

    def get_content(self): # this methods needs to be filled for the actual pages
        sleep(3)
        st.warning(f"No content implemented for {self.__class__.__name__}")


def set_sidebar_width(width=500):
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: ###px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: ###px;
        margin-left: -###px;
        }
        </style>
        """.replace("###", str(width)),
        unsafe_allow_html=True
    )