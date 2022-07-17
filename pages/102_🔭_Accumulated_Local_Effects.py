import streamlit as st
from content.layout import BasePage
from content.model_utils import get_model, get_X
from content.plot_utils import display_figure
from alibi.explainers import ALE
from alibi.explainers import plot_ale


class AccumulatedLocalEffectsPage(BasePage):
    def __init__(self):
        super().__init__(
            title = "Accumulated Local Effects",
            depends = {"model", "X"},
        )

    def get_content(self):
        model = get_model()
        X = get_X().reset_index(drop=True)
        
        feature = st.selectbox("Feature", X.columns)
        
        if st.button("Calculate Plot"):
            with st.spinner(f"Preparing {self.title}..."):
                ale = ALE(model.predict, feature_names=X.columns)#, target_names=target_names)
                exp = ale.explain(X, features=[feature])
                plot_ale(exp)
                display_figure()


AccumulatedLocalEffectsPage()
