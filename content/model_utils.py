import streamlit as st
import pandas as pd

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