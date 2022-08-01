import streamlit as st
from matplotlib import pyplot as plt
import mplcyberpunk
from io import BytesIO


def activate_neon_plots():
    plt.style.use("cyberpunk")

def display_figure():
    mplcyberpunk.make_lines_glow()
    # save to buffer early to avoid transparent background
    fig = plt.gcf()
    img = BytesIO()
    plt.savefig(img, format="png")
    st.session_state["img"] = img
    # make background and canvas transparent
    fig.patch.set_facecolor('b')
    fig.patch.set_alpha(0)
    ax = plt.gca()
    ax.patch.set_facecolor('b')
    ax.patch.set_alpha(0)
    # display and close
    st.pyplot(fig)
    plt.close()
