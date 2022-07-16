import streamlit as st
from content.layout import set_sidebar_width
from content.global_methods.Partial_Dependence_Plots import PartialDependencePlotsPage
from content.global_methods.Accumulated_Local_Effects import AccumulatedLocalEffectsPage
from content.global_methods.Feature_Interaction import FeatureInteractionPage
from content.global_methods.Functional_Decomposition import FunctionalDecompositionPage
from content.global_methods.Global_Surrogate import GlobalSurrogatePage
from content.global_methods.Permutation_Feature_Importance import PermutationFeatureImportancePage


set_sidebar_width(400)


st.title("Global Methods")
st.sidebar.header("Global Methods")
st.sidebar.write("Explain overall patterns.")
