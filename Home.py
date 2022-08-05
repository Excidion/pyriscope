import streamlit as st
from content.plot_utils import activate_neon_plots

activate_neon_plots()


st.title("Pyriscope")
st.caption("Take a look into your black box models.")
st.write(
    "This application tries to help you to get to know your Machine Learning Models. "
    "For this reason it contains tools und methods to help you anderstand or debug any model - regardless of its structure. "
    "As long as your model is a python object with a `predict()` method, this app will be able to work with it. "
    "The goal is that you and your models users take a look into the models inner workings to grow trust into the model and its predictions. "
)
st.write("The application is separated into four main sections:")

st.subheader("Settings")
st.write("For uploading your model and data - this should be your first step.")

st.subheader("Explore Model")
st.write("Take a look at your model and try out how different input values influence prediction results.")

st.subheader("Global Methods 🔭")
st.write(   
    "Tools and Methods to understand which general patterns the model has learned. ", 
    "Global interpretation methods describe average behavior, they are particularly useful when you want to understand the general mechanisms in the data or debug a model. "
)

st.subheader("Local Methods 🔬")
st.write(
    "Tools and Methods to understand why a specific prediction was made. ",
    "Local interpretation methods explain individual predictions. "
)
