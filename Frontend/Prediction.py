import streamlit as st
from PIL import Image #type: ignore

from Utils.ModelUtils import (load_model, predict, generate_gradcam, TARGET_COLUMNS)
from Utils.DashboardUtils import (render_dashboard) #type: ignore
from Utils.RecomendationUtils import (render_recommendations, generate_summary)
from Utils.ReportUtils import (generate_pdf_report, download_report)

MODEL_PATH = r"Models\model.pth"

def show():
    st.title("🔍 AI Biomass Prediction Dashboard")
    st.write(
                """
                Upload a pasture RGB image to estimate biomass,
                visualize model explainability,
                receive AI-generated recommendations,
                and generate a complete biomass assessment report.
                """
    )
    st.divider()

    defaults = {"prediction_done": False, "predictions": None, "heatmap": None, "overlay": None, "summary": None, "health_score": None, "field_status": None}

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    @st.cache_resource
    def get_model():
        return load_model(MODEL_PATH)
    model = get_model()


    uploaded_file = st.file_uploader("Upload Pasture Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is None:
        st.info("Please upload an RGB pasture image.")
        return

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.divider()


    if st.button("🌿 Predict Biomass", use_container_width=True):
        with st.spinner("Running EfficientNet-B3..."):
            predictions = predict(model, image)
            st.session_state.predictions = predictions

            st.session_state.prediction_done = True
            st.session_state.heatmap = None
            st.session_state.overlay = None

    if st.session_state.prediction_done:
        predictions = st.session_state.predictions        
        st.success("Prediction Completed Successfully.")
        st.divider()

        render_dashboard(predictions)
        st.divider()

        render_recommendations(predictions)
        st.divider()

        score = min(100, max(0, predictions["Dry Total (g)"] / 1000 * 100))

        if predictions["Dry Total (g)"] >= 700:
            field_status = "🟢 Excellent"

        elif predictions["Dry Total (g)"] >= 400:
            field_status = "🟡 Moderate"

        else:
            field_status = "🔴 Poor"

        summary = generate_summary(predictions)
        pdf = generate_pdf_report(predictions, score, field_status, summary)

        st.subheader("📄 AI Report")
        st.write(
                    """
                    Download a complete biomass assessment report
                    containing predictions, field status and
                    AI-generated recommendations.
                    """
        )
        download_report(pdf)
        st.divider()

        st.subheader("Model Explainability")
        st.write(
                    """
                    Select one of the predicted biomass outputs to visualize
                    the image regions that contributed most to the prediction.
                    """
        )

        selected_target = st.selectbox("Select Biomass Output", TARGET_COLUMNS, key="gradcam_target")

        if st.button("Generate Grad-CAM", use_container_width=True):
            try:
                target_index = TARGET_COLUMNS.index(selected_target)

                with st.spinner("Generating Manual Grad-CAM..."):
                    heatmap, overlay = generate_gradcam(model, image, target_index)

                st.session_state.heatmap = heatmap
                st.session_state.overlay = overlay

                st.success("Grad-CAM Generated Successfully.")

            except Exception as e:
                st.error("Unable to generate Grad-CAM.")
                st.exception(e)


        if (st.session_state.heatmap is not None and st.session_state.overlay is not None):
            st.divider()
            st.subheader("Grad-CAM Visualization")
            c1, c2, c3 = st.columns(3)

            with c1:
                st.image(image, caption="Original Image", use_container_width=True)

            with c2:
                st.image(st.session_state.heatmap, caption="Activation Heatmap", use_container_width=True)

            with c3:
                st.image(st.session_state.overlay, caption="Grad-CAM Overlay", use_container_width=True)

            st.info(
                    f"""
                    The highlighted regions indicate the areas that most strongly
                    influenced the prediction for **{selected_target}**.
                    Lighter colors represent regions with higher contribution
                    towards the predicted biomass.
                    """
            )
        st.divider()
            
        with st.expander("Prediction Summary", expanded=False):
            st.markdown(
                        """
                        ### AI Processing Pipeline

                        ✔ Image Preprocessing

                        ✔ EfficientNet-B3 Feature Extraction

                        ✔ Multi-Output Biomass Regression

                        ✔ Dashboard Visualization

                        ✔ AI Decision Support

                        ✔ Manual Grad-CAM Explainability

                        ✔ PDF Report Generation
                        """
            )

        with st.expander("Model Information", expanded=False):
            c1, c2 = st.columns(2)

            with c1:
                st.metric("Architecture", "EfficientNet-B3")
                st.metric("Framework", "PyTorch")
                st.metric("Task", "Multi-Output Regression")

            with c2:
                st.metric("Outputs", "5")
                st.metric("Explainability", "Manual Grad-CAM")
                st.metric("Deployment", "Streamlit")

        with st.expander("Project Outcomes", expanded=False):
            outcomes = [
                        "Automated biomass estimation from pasture images",
                        "Near real-time field assessment",
                        "Biomass heatmap visualization",
                        "AI-assisted grazing recommendations",
                        "Feed planning support",
                        "Precision agriculture support",
                        "Automated report generation"
            ]

            for outcome in outcomes:
                st.success(outcome)

        st.divider()
        st.caption(
                    """
                    AI-Based Pasture Biomass Monitoring and Decision Support System

                    Powered by EfficientNet-B3, PyTorch, Manual Grad-CAM and Streamlit.
                    """
        )