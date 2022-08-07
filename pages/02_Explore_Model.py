import streamlit as st
from content.model_utils import get_model, get_X, get_y, get_model_params, model_input_form
from sklearn.metrics import get_scorer, get_scorer_names
import pandas as pd

st.title("Explore Model")

st.header("Info")
model = get_model()
if model is None:
    st.warning("No model has been uploaded.")
else:
    with st.expander("Model details"):    
        st.code(repr(model))
        params = get_model_params(model)
        if params is None:
            st.write(f"No method for extracting parameters for mode class `{model.__class__.__name__}`")
        else:
            st.write("with the following parameters")
            st.json(params)


X = get_X()
if X is None:
    st.warning("No data has been uploaded.")
else:
    with st.expander("Inspect data"):
        st.dataframe(X)

y = get_y()
if y is None:
    st.warning("No labels has been uploaded.")


if model is not None and X is not None and y is not None:
    with st.expander("Scoring"):
        scorer_name = st.selectbox("Scoring method", get_scorer_names())
        scorer = get_scorer(scorer_name)
        st.info(f"{scorer_name} on uploaded dataset is {round(scorer(model, X, y), 2)}")


st.header("Try predictions")
if model is not None and X is not None and y is not None:
    settings, X_pred = model_input_form(X)
    col1, col2 = st.columns(2)
    with col1:
        st.caption("Input values")
        st.json(settings)
    with col2:
        st.caption("Output")
        st.code(f"{model.predict(X_pred.values.reshape(1, -1))}")
