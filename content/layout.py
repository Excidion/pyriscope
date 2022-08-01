import streamlit as st
from time import sleep
from content.model_utils import get_session_data

class BasePage:
    def __init__(self, title, depends={"model"}):
        self.title = title
        self.depends = depends
        self.build_page()
    
    def build_page(self):
        st.session_state["img"] = None # reset image cache
        # check all required files have been uploaded
        none_missing = True
        for i in self.depends:
            if not i in st.session_state.keys():
                none_missing = False
                st.warning(f"{self.title} requires {self.depends}. Please upload missing {i} in the 'Settings' page.")
        # if all required uploads are there, display the page content
        if none_missing:
            st.title(self.title)
            self.get_content()
            # if there has been an image generated and cached offer download
            img = get_session_data("img")
            st.download_button(
                label = "Download Plot",
                data = img if img is not None else "",
                file_name = self.title.replace(" ", "-") + ".png",
                mime = "image/png",
                disabled = img is None,
            )

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