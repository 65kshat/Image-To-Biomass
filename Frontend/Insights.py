
import streamlit as st
import pandas as pd #type: ignore
import matplotlib.pyplot as plt

from Utils.ModelUtils import PROJECT_INFORMATION

def show():
    st.title("📊 Project Insights")

    training = pd.read_csv(r"Dataset\training_history.csv")
    metrics = pd.read_csv(r"Dataset\evaluation_metrics.csv")

    st.subheader("Model Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("Model", PROJECT_INFORMATION["Model"])
    col2.metric("Training Images", PROJECT_INFORMATION["Training Images"])
    col3.metric("Validation Images", PROJECT_INFORMATION["Validation Images"])

    st.divider()

    st.subheader("Training History")
    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(training["train_loss"], label="Training Loss")
    ax.plot(training["valid_loss"], label="Validation Loss")

    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.legend()

    st.pyplot(fig)
    st.divider()

    st.subheader("Evaluation Metrics")

    st.dataframe(metrics, use_container_width=True)

    st.divider()

    st.subheader("RMSE Comparison")
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(metrics["Target"], metrics["RMSE"])

    plt.xticks(rotation=25)
    st.pyplot(fig)
    st.divider()

    st.subheader("Project Summary")

    st.markdown("""
                ### Key Findings

                - EfficientNet-B3 was used as the backbone model.
                - Transfer learning enabled effective regression with a relatively small dataset.
                - The model predicts **five biomass parameters** simultaneously.
                - Best performance was obtained after **50 epochs**.
                - Training and validation losses converged smoothly, indicating stable learning.
                - Evaluation metrics demonstrate good regression performance for this dataset.
    """)