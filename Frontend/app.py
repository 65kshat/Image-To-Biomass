import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

import Home
import Prediction
import Insights

st.set_page_config(page_title="Image-to-Biomass Prediction System", page_icon="🌿", layout="wide", initial_sidebar_state="expanded")


st.sidebar.title("🌿 Navigation")
page = st.sidebar.radio("Select Page", ("🏠 Home", "🔍 Prediction", "📊 Project Insights"))
st.sidebar.divider()

st.sidebar.markdown(
                    """
                    ### Project Information

                    **Model**
                    - EfficientNet-B3

                    **Task**
                    - Multi-Output Image Regression

                    **Framework**
                    - PyTorch

                    **Frontend**
                    - Streamlit

                    **Explainability**
                    - Manual Grad-CAM
                    """

)

st.sidebar.divider()

st.sidebar.info("AI-Based Pasture Biomass Monitoring and Decision Support System")

if page == "🏠 Home":
    Home.show()

elif page == "🔍 Prediction":
    Prediction.show()

elif page == "📊 Project Insights":
    Insights.show()

st.sidebar.divider()

st.sidebar.caption("Developed using PyTorch, Streamlit and EfficientNet-B3")