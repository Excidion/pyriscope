import sys
import pathlib
sys.path.append(str(pathlib.Path().absolute())) # fix imports for streamlit
import streamlit as st
from content.layout import BasePage

class ScopedRulesPage(BasePage):
    def __init__(self):
        super().__init__(title="Scoped Rules")

    def get_content(self):
        st.info("Placeholder")
