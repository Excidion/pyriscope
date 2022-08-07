import streamlit as st
from content.layout import BasePage
from content.model_utils import get_model, get_X, get_y, get_output_type, log10_sampling_slider
from sklearn.inspection import PartialDependenceDisplay
from content.plot_utils import display_figure


class IndividualConditionalExpectationPage(BasePage):
    def __init__(self):
        super().__init__(
            title = "Individual Conditional Expectation Plots",
            depends = {"model", "X", "y"}
        )

    def get_content(self):
        st.write(
            "TBD"
        )
        model = get_model()
        X = get_X()

        if get_output_type() == "multiclass-classification": # check for multiclass
            y = get_y()
            target = st.selectbox("Target", y.unique())
        else:
            target = None
        
        feature = st.selectbox("Feature", X.columns)
        features = [feature]

        samples = log10_sampling_slider(maxsize=len(X))

        centered = st.checkbox(
            "Center plot", 
            help = "Makes sure the graph starts at `(x=0, y=0)`."
        )

        if st.button("Calculate Plot"):
            with st.spinner(f"Preparing {self.title}..."):
                PartialDependenceDisplay.from_estimator(
                    model, 
                    X, 
                    features, 
                    target = target, 
                    kind = "individual", 
                    n_jobs = -1,
                    subsample = int(samples),
                    centered = centered,
                )
                display_figure()


IndividualConditionalExpectationPage()