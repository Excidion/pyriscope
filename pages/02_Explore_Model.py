import streamlit as st
from content.model_utils import get_model, get_X, get_y, undummify, get_model_params
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
    settings = dict()
    with st.expander("Change Input values"):
        with st.form("Change Input values"):
            with st.spinner("Loading input variables"):
                X_og = undummify(X)
                for i, var_name in enumerate(X_og.columns):
                    var_data = X_og[var_name]
                    dtype = var_data.dtype
                    if dtype == "object":
                        settings[var_name] = st.selectbox(var_name, var_data.unique())
                    elif dtype == "int":
                        lower = int(var_data.min())
                        upper = int(var_data.max())
                        default = int(var_data.median())
                        settings[var_name] = st.slider(var_name, min_value=lower, max_value=upper, value=default, step = 1)
                    elif dtype == "float":
                        lower = float(var_data.min())
                        upper = float(var_data.max())
                        default = float(var_data.median())
                        settings[var_name] = st.slider(var_name, min_value=lower, max_value=upper, value=default)
                    else:
                        st.error(f"Problem with {var_name}: Selector for dtype {dtype} not implemented.")
            st.form_submit_button("Make prediction")
    
    col1, col2 = st.columns(2)
    with col1:
        st.caption("Input values")
        st.json(settings)
    with col2:
        st.caption("Output")
        X_pred = pd.get_dummies(X_og.append(settings, ignore_index=True)) # connect with X_og to have consistent dummy columns
        X_pred = X_pred[X.columns] # ensure the right order of columns
        X_pred = X_pred.iloc[-1]
        st.code(f"{model.predict(X_pred.values.reshape(1, -1))}")
