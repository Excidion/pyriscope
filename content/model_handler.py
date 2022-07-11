import sys
import pathlib
sys.path.append(str(pathlib.Path().absolute())) # fix imports for streamlit
import streamlit as st
from content.layout import BasePage
from joblib import load


class ModelHandlerPage(BasePage):

    def __init__(self):
        super().__init__(title="Settings")


    def get_content(self):
        with st.form("settings"):

            with st.container():
                st.header("Upload a model")
                st.write("Save your model to disk with the following command:")
                st.code('''
                    from joblib import dump
                    \ndump(model, "model.pkl")
                ''')
                st.markdown("A model can be any python object that has a `predict` method.")

                model = st.file_uploader(
                    "Choose a model file",
                    type = ["pkl", "pickle"]
                )
                if model is not None:
                    st.session_state["model"] = load(model)
            st.markdown("""---""")

            st.header("Upload the test-dataset")
            st.write("Before training the model, you probalby split your dataset like")
            st.code('''
                from sklearn.model_selection import train_test_split
                \nX_train, X_test, y_train, y_test = tran_test_split(X, y)
                \nX_test.to_parquet("X_test.pq")
                \ny_test.to_parquet("y_test.pq")
            ''')

            data, label = st.columns(2)
            
            with data:
                st.markdown("Upload `X_test.pq` here:")
                X = st.file_uploader(
                    "Choose a data file",
                    type = ["pq", "parquet"]
                )
                if not X is None:
                    st.session_state["X"] = load(X)

            with label:
                st.markdown("Upload `y_test.pq` here:")
                y = st.file_uploader(
                    "Choose a label file",
                    type = ["pq", "parquet"]
                )
                if not y is None:
                    st.session_state["y"] = load(y)

            st.form_submit_button("Upload model and data.")
