from multiprocessing.sharedctypes import Value
import streamlit as st
import pandas as pd
from math import log10


def log10_sampling_slider(maxsize):
    slider = st.select_slider(
        label = "Sample Size",
        options = [10**m for m in range(int(log10(maxsize)) + 1)] + [maxsize],
        value = maxsize,
        help = "This calculation might take some time and can be most easily sped up adjusting the number of samples from `X` used."
    )
    return slider


def get_output_type():
    y = get_y()
    if y.dtype == "object":
        if y.nunique() > 2:
            return "multiclass-classification"
        else:
            return "classification"
    elif y.dtype == "float":
        return "regression"
    else:
        raise ValueError(f"Outpuy type for {y.dtype} not defined.")       


def get_model_params(model=None):
    if model is None:
        model = get_model()
    try: # sklearn style 
        return model.get_params()
    except AttributeError:
        return None


def get_model():
    return get_session_data("model")

def get_X():
    return get_session_data("X")

def get_y():
    return get_session_data("y")

def get_session_data(key):
    try:
        return st.session_state.get(key)
    except KeyError:
        return None


def model_input_form(X):
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

    X_pred = pd.get_dummies(X_og.append(settings, ignore_index=True)) # connect with X_og to have consistent dummy columns
    X_pred = X_pred[X.columns] # ensure the right order of columns
    X_pred = X_pred.iloc[-1]
    return settings, X_pred

def undummify(df, prefix_sep="_"):
    cols2collapse = {
        item.split(prefix_sep)[0]: (prefix_sep in item) for item in df.columns
    }
    series_list = []
    for col, needs_to_collapse in cols2collapse.items():
        if needs_to_collapse:
            undummified = (
                df.filter(like=col)
                .idxmax(axis=1)
                .apply(lambda x: x.split(prefix_sep, maxsplit=1)[1])
                .rename(col)
            )
            series_list.append(undummified)
        else:
            series_list.append(df[col])
    undummified_df = pd.concat(series_list, axis=1)
    return undummified_df
