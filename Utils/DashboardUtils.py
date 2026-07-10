import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd #type: ignore
import numpy as np

from datetime import datetime

HEALTH_THRESHOLDS = {"Excellent": 700, "Moderate": 400, "Poor": 0}

def display_prediction_metrics(predictions):
    st.subheader("🌿 Biomass Prediction Results")
    c1, c2 = st.columns(2)
    items = list(predictions.items())

    for i in range(3):
        c1.metric(items[i][0], f"{items[i][1]:.2f} g")

    for i in range(3,5):
        c2.metric(items[i][0], f"{items[i][1]:.2f} g")


def calculate_health_score(predictions):
    dry_total = predictions["Dry Total (g)"]
    score = min(100, max(0, (dry_total / 1000) * 100))

    return round(score,1)

def classify_field(predictions):
    biomass = predictions["Dry Total (g)"]

    if biomass >= HEALTH_THRESHOLDS["Excellent"]:
        return ("🟢 Excellent", "Excellent biomass production.")

    elif biomass >= HEALTH_THRESHOLDS["Moderate"]:
        return ("🟡 Moderate", "Pasture requires monitoring.")

    else:
        return ("🔴 Poor", "Pasture recovery recommended.")

def display_dashboard_summary(predictions):
    score = calculate_health_score(predictions)
    status, message = classify_field(predictions)

    st.subheader("Field Health Dashboard")
    c1, c2 = st.columns(2)

    with c1:
        st.metric("Health Score", f"{score:.1f}/100")

    with c2:
        st.metric("Field Status", status)

    if score >= 70:
        st.success(message)

    elif score >= 40:
        st.warning(message)

    else:
        st.error(message)

def plot_biomass_bar(predictions):
    st.subheader("Biomass Distribution")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(predictions.keys(), predictions.values())

    ax.set_ylabel("Biomass (g)")
    ax.set_title("Predicted Biomass")

    plt.xticks(rotation=20)
    plt.tight_layout()
    st.pyplot(fig)

def plot_biomass_pie(predictions):
    st.subheader("Biomass Composition")

    values = np.array(list(predictions.values()))
    labels = list(predictions.keys())
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

def display_prediction_table(predictions):
    st.subheader("Prediction Summary")

    df = pd.DataFrame({"Biomass Type": list(predictions.keys()), "Predicted Value (g)": list(predictions.values())})
    st.dataframe(df, use_container_width=True, hide_index=True)

    return df

def display_statistics(predictions):
    values = np.array(list(predictions.values()))

    st.subheader("Prediction Statistics")
    c1, c2, c3 = st.columns(3)

    c1.metric("Average", f"{values.mean():.2f} g")
    c2.metric("Maximum", f"{values.max():.2f} g")
    c3.metric("Minimum", f"{values.min():.2f} g")

    st.caption("Statistics computed across all predicted biomass outputs.")

def update_prediction_history(predictions):
    if "prediction_history" not in st.session_state:
        st.session_state.prediction_history = []

    record = {"Timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

    record.update(predictions)
    st.session_state.prediction_history.append(record)


def display_prediction_history():
    if ("prediction_history" not in st.session_state):
        return

    history = pd.DataFrame(st.session_state.prediction_history)

    st.subheader("Prediction History")
    st.dataframe(history, use_container_width=True, hide_index=True)


def display_dashboard_info():
    st.subheader("AI Dashboard")
    c1, c2, c3 = st.columns(3)

    c1.metric("Model", "EfficientNet-B3")
    c2.metric("Framework", "PyTorch")
    c3.metric("Outputs", "5")
    c1.metric("Image Size", "256 × 512")
    c2.metric("Explainability", "Grad-CAM")
    c3.metric("Deployment", "Streamlit")


def display_footer():
    st.divider()
    st.success(
                """
                Automated Biomass Estimation
                Explainable AI
                Multi-Output Regression
                Precision Agriculture Support
                Decision Support Ready
                """
    )


def render_dashboard(predictions):
    update_prediction_history(predictions)
    display_prediction_metrics(predictions)
    display_dashboard_summary(predictions)
    plot_biomass_bar(predictions)
    plot_biomass_pie(predictions)
    display_prediction_table(predictions)
    display_statistics(predictions)

    display_prediction_history()
    display_dashboard_info()
    display_footer()