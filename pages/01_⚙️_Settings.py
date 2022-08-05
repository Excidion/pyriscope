import streamlit as st
from cloudpickle import load
import pandas as pd


st.title("Settings")

with st.container():
    st.header("Upload a model")
    st.write("Save your model to disk with the following command:")
    st.code("""
        from cloudpickle import dump
        \nwith open("model.cldpkl", "wb") as filecontent:\n\tdump(model, filecontent)
    """)
    st.markdown("A model can be any python object that has a `predict` method.")

    model = st.file_uploader(
        "Choose a model file",
        type = ["cldpkl", "cloudpickle"]
    )
    if model is not None:
        with st.spinner("Processing `model`"):
            st.session_state["model"] = load(model)
            st.info("Done.")

st.header("Upload the test-dataset")
st.write("Before training the model, you probalby split your dataset like")
st.code('''
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)

X_test.to_parquet("X_test.pq")
pd.DataFrame(y_test).to_parquet("y_test.pq")
''')

data, label = st.columns(2)

with data:
    st.markdown("Upload `X_test.pq` here:")
    X = st.file_uploader(
        "Choose a data file",
        type = ["pq", "parquet"]
    )
    if X is not None:
        with st.spinner("Processing `X`"):
            st.session_state["X"] = pd.read_parquet(X)
            st.info("Done.")
    

with label:
    st.markdown("Upload `y_test.pq` here:")
    y = st.file_uploader(
        "Choose a label file",
        type = ["pq", "parquet"]
    )
    if y is not None:
        with st.spinner("Processing `y`"):
            st.session_state["y"] = pd.read_parquet(y).iloc[:, 0]
            st.info("Done.")