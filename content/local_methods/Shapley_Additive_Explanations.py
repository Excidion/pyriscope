import sys
import pathlib
sys.path.append(str(pathlib.Path().absolute())) # fix imports for streamlit
import streamlit as st
from content.layout import BasePage

class ShapleyAdditiveExplanationsPage(BasePage):
    def __init__(self):
        super().__init__(title="Shapley Additive Explanations")

    def get_content(self):
        st.info("Placeholder")
