import streamlit as st
from matplotlib import pyplot as plt
import mplcyberpunk


def activate_neon_plots():
    plt.style.use("cyberpunk")

def display_figure():
    mplcyberpunk.add_glow_effects()
    st.pyplot(plt.gcf())
    plt.close()
