from multiprocessing.sharedctypes import Value
import streamlit as st
import pandas as pd
from math import log10


def log10_sampling_slider(maxsize):
    slider = st.select_slider(
        label = "Sample Size",
        options = [10**m for m in range(int(log10(maxsize)) + 1)] + [maxsize],
        value = maxsize,
        help = "This calculation might take some minutes and ca be most easily reduced by adjusting the number of samples from `X` used."
    )
    return slider


def get_output_type():
    y = get_y()
    if y.dtype == "object":
        if y.nunique() > 2:
            return "multilabel-classification"
        else:
            return "classification"
    elif y.dtype == "float":
        return "regression"
    else:
        raise ValueError(f"Outpuy type for {y.dtype} not defined.")       


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
