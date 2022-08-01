import streamlit as st
from matplotlib import pyplot as plt
import mplcyberpunk


def activate_neon_plots():
    plt.style.use("cyberpunk")

def display_figure():
    mplcyberpunk.make_lines_glow()
    fig = plt.gcf()
    fig.patch.set_facecolor('b')
    fig.patch.set_alpha(0)
    ax = plt.gca()
    ax.patch.set_facecolor('b')
    ax.patch.set_alpha(0)
    st.pyplot(fig)
    plt.close()
