import streamlit as st
from content.layout import BasePage, set_sidebar_width
from content.global_methods.Partial_Dependence_Plots import PartialDependencePlotsPage
from content.global_methods.Accumulated_Local_Effects import AccumulatedLocalEffectsPage
from content.global_methods.Feature_Interaction import FeatureInteractionPage
from content.global_methods.Functional_Decomposition import FunctionalDecompositionPage
from content.global_methods.Global_Surrogate import GlobalSurrogatePage
from content.global_methods.Permutation_Feature_Importance import PermutationFeatureImportancePage
from content.local_methods.Individual_Conditional_Expectation_Curves import IndividualConditionalExpectationCurvesPage
from content.local_methods.Local_Surrogate_Models import LocalSurrogateModelsPage
from content.local_methods.Counterfactual_Explanations import ConterfactualExplanationsPage
from content.local_methods.Scoped_Rules import ScopedRulesPage
from content.local_methods.Shapley_Values import ShapleyValuesPage
from content.local_methods.Shapley_Additive_Explanations import ShapleyAdditiveExplanationsPage


set_sidebar_width(350)

with st.sidebar.title("Periscope"):
    st.sidebar.write("Take a look into your black box model.")
    st.sidebar.markdown("""---""") 

with st.sidebar.header("Model"):
    #st.sidebar.write("")
    BasePage("Upload a model")
    BasePage("Test the model")
    st.sidebar.markdown("""---""") 

with st.sidebar.header("Global Methods"):
    st.sidebar.write("Explain overall patterns.")
    PartialDependencePlotsPage()
    AccumulatedLocalEffectsPage()
    FeatureInteractionPage()
    FunctionalDecompositionPage()
    GlobalSurrogatePage()
    PermutationFeatureImportancePage()
    st.sidebar.markdown("""---""") 

with st.sidebar.header("Local Methods"):
    st.sidebar.write("Explain single predictions.")
    IndividualConditionalExpectationCurvesPage()
    LocalSurrogateModelsPage()
    ConterfactualExplanationsPage()
    ScopedRulesPage()
    ShapleyValuesPage()
    ShapleyAdditiveExplanationsPage()
    st.sidebar.markdown("""---""") 
