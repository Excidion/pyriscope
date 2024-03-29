import streamlit as st
from content.layout import BasePage
from content.model_utils import get_model, get_X, get_y, get_output_type, log10_sampling_slider
from sklearn.inspection import PartialDependenceDisplay
from content.plot_utils import display_figure


class PartialDependencePlotsPage(BasePage):
    def __init__(self):
        super().__init__(
            title = "Partial Dependence Plots",
            depends = {"model", "X", "y"}
        )

    def get_content(self):
        st.write(
            "The partial dependence plot (short PDP or PD plot) shows the marginal effect one or two features have on the predicted outcome of a machine learning model. ",
            "A partial dependence plot can show whether the relationship between the target and a feature is linear, monotonic or more complex. ",
            "For example, when applied to a linear regression model, partial dependence plots always show a linear relationship."
            "For more detailed explainations follow this [link](https://christophm.github.io/interpretable-ml-book/pdp.html#pdp)"
        )
        model = get_model()
        X = get_X()

        if get_output_type() == "multiclass-classification": # check for multiclass
            y = get_y()
            target = st.selectbox("Target", y.unique())
        else:
            target = None
        
        plot_type = st.selectbox("Type of Plot", ["1-dimensional", "2-dimensional"])
        if plot_type == "1-dimensional":
            feature = st.selectbox("Feature", X.columns)
            features = [feature]
        if plot_type == "2-dimensonal":
            feature1 = st.selectbox("Feature 1", X.columns)
            feature2 = st.selectbox("Feature 2", X.columns)
            features = [(feature1, feature2)]

        samples = log10_sampling_slider(maxsize=len(X))

        centered = st.checkbox(
            "Center plot", 
            help = "Makes sure the graph starts at `(0,0)`."
        )

        if st.button("Calculate Plot"):
            with st.spinner(f"Preparing {self.title}..."):
                PartialDependenceDisplay.from_estimator(
                    model, 
                    X.sample(samples), 
                    features, 
                    target = target, 
                    n_jobs = -1,
                    centered = centered,
                )
                display_figure()


PartialDependencePlotsPage()
