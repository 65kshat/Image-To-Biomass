import streamlit as st

def show():
    st.title("🌿 AI-Based Pasture Biomass Monitoring System")

    st.markdown(
                """
                Welcome to the **Image-to-Biomass Prediction System**.

                This application utilizes **Deep Learning**, **Computer Vision**, and
                **Explainable Artificial Intelligence (XAI)** to estimate pasture biomass
                directly from RGB field images. The system predicts five biomass components,
                visualizes model attention using **Manual Grad-CAM**, and provides intelligent
                recommendations to support pasture management and precision agriculture.
                """
    )

    st.divider()
    st.subheader("Key Features")
    c1, c2 = st.columns(2)

    with c1:
        st.success("Automated Biomass Estimation")

        st.write(
                    """
                    Predicts:
                    • Dry Clover
                    • Dry Dead
                    • Dry Green
                    • Dry Total
                    • GDM
                    """         
        )

        st.success("Explainable AI")

        st.write(
                    """
                    Manual Grad-CAM highlights the image regions
                    contributing most to biomass prediction.
                    """
                )

        st.success("Interactive Dashboard")

        st.write(
                    """
                    Visualize predictions using

                    • Dashboard Metrics
                    • Bar Charts
                    • Pie Charts
                    • Prediction History
                    """
        )

    with c2:
        st.success("Decision Support")
        st.write(
                """
                AI-assisted recommendations for

                • Grazing
                • Feed Planning
                • Monitoring
                """
        )

        st.success("Report Generation")
        st.write(
                    """
                    Export complete AI-generated
                    biomass assessment reports.
                    """
        )

        st.success("Precision Agriculture")
        st.write(
                    """
                    Supports modern agricultural workflows through

                    • Automated Analysis
                    • Decision Support
                    • Explainability
                    • Reporting
                    """
        )

    st.divider()

    st.subheader("System Workflow")

    st.markdown("""
    ```
    Upload Field Image
            │
            ▼
    Deep Learning Prediction
            │
            ▼
    Biomass Estimation
            │
            ▼
    AI Dashboard
            │
            ▼
    Grad-CAM Explainability
            │
            ▼
    Decision Support
            │
            ▼
    Download Report
    ```
    """)

    st.divider()

    st.subheader("🛠 Technologies Used")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(
                """
                **Artificial Intelligence**

                • PyTorch
                • EfficientNet-B3
                • Transfer Learning
                • Multi-Output Regression
                """
        )

    with c2:
        st.info(
                """
                **Data Science**

                • NumPy
                • Pandas
                • Matplotlib
                • OpenCV
                """
        )

    with c3:
        st.info(
                """
                **Application**

                • Streamlit
                • ReportLab
                • Manual Grad-CAM
                • Python
                """
        )

    st.divider()

    st.subheader("Project Outcomes")
    outcomes = [
        "Automated biomass estimation from pasture images",
        "Near real-time field assessment",
        "Biomass heatmap visualization using Manual Grad-CAM",
        "AI-assisted grazing and feed planning",
        "Reduced manual survey effort",
        "Support for precision agriculture"
    ]

    for outcome in outcomes:
        st.success(f"✔ {outcome}")

    st.divider()

    st.caption("Developed as an AI & Data Science Deep Learning Project using EfficientNet-B3 and Streamlit.")