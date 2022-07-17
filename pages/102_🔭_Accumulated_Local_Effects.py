import streamlit as st
from content.layout import BasePage
from content.model_utils import get_model, get_X, get_y, log10_sampling_slider, get_output_type
from content.plot_utils import display_figure
from alibi.explainers import ALE
from alibi.explainers import plot_ale
from sklearn.preprocessing import LabelBinarizer
import numpy as np

class AccumulatedLocalEffectsPage(BasePage):
    def __init__(self):
        super().__init__(
            title = "Accumulated Local Effects",
            depends = {"model", "X", "y"},
        )

    def get_content(self):
        st.write(
            "Due to is mathematical definition Partial Dependence Plots are problematic when features are correlated."
            "Accumulated Local Effects is are more appropirate alternative in case features might be correlated."
            "For the mathematical detail follow this [link](https://docs.seldon.io/projects/alibi/en/stable/methods/ALE.html#Motivation-and-definition)."
        )

        X = get_X()
        feature = st.selectbox("Feature", X.columns)
        features = [i for i, f in enumerate(X.columns) if f == feature]
        samples = log10_sampling_slider(maxsize=len(X))

        if get_output_type() == "multiclass-classification": # check for multiclass
            y = get_y()
            labeler = LabelBinarizer()
            labeler.fit(y)
            ident = np.identity(y.nunique()).astype(int)
            target_names = labeler.inverse_transform(ident)
        else:
            labeler = None
            target_names = None

        model = get_model()

        if st.button("Calculate Plot"):
            with st.spinner(f"Preparing {self.title}..."):
                ale = ALE(
                    lambda x: labeler.transform(model.predict(x)) if labeler is not None else model.predict(x), 
                    feature_names=X.columns, 
                    target_names=target_names
                )
                exp = ale.explain(X.sample(samples).values, features=features)
                plot_ale(exp)
                display_figure()


AccumulatedLocalEffectsPage()
