import streamlit as st

EXCELLENT_THRESHOLD = 700
MODERATE_THRESHOLD = 400

def get_field_status(predictions):
    biomass = predictions["Dry Total (g)"]

    if biomass >= EXCELLENT_THRESHOLD:
        return ("🟢 Excellent", "High")

    elif biomass >= MODERATE_THRESHOLD:
        return ("🟡 Moderate", "Medium")

    else:
        return ("🔴 Poor", "Low")


def grazing_recommendation(predictions):
    biomass = predictions["Dry Total (g)"]

    if biomass >= EXCELLENT_THRESHOLD:
        return {
            "title": "Continue Grazing",
            "message":
            """
            Biomass availability is excellent.
            Livestock can continue grazing normally.
            Routine field monitoring is recommended.
            """
        }

    elif biomass >= MODERATE_THRESHOLD:
        return {
            "title": "Rotational Grazing",
            "message":
            """
            Moderate biomass detected.
            Rotate livestock between paddocks.
            Avoid overgrazing.
            """
        }

    else:
        return {
            "title": "Rest Pasture",
            "message":
            """
            Low biomass detected.
            Suspend grazing temporarily.
            Allow vegetation recovery.
            """
        }


def feed_recommendation(predictions):
    biomass = predictions["Dry Total (g)"]

    if biomass >= EXCELLENT_THRESHOLD:
        return ("No Supplement Required", "Current pasture can sustain grazing.")

    elif biomass >= MODERATE_THRESHOLD:
        return ("Partial Supplement", "Provide supplemental feed during grazing.")

    else:
        return ("Full Supplement", "Supplemental feeding is strongly recommended.")


def monitoring_interval(predictions):
    biomass = predictions["Dry Total (g)"]

    if biomass >= EXCELLENT_THRESHOLD:
        return "Monitor every 7 days."

    elif biomass >= MODERATE_THRESHOLD:
        return "Monitor every 3 days."

    else:
        return "Daily monitoring is recommended."


def estimate_savings():
    manual_time = 20      
    ai_time = 0.5             
    saved = manual_time - ai_time

    return {
        "Manual Survey": f"{manual_time} minutes",
        "AI Prediction": f"{ai_time} minutes",
        "Time Saved": f"{saved:.1f} minutes"
    }


def precision_checklist():
    return [
        "Automated Biomass Estimation",
        "Explainable AI (Grad-CAM)",
        "Pasture Health Assessment",
        "Grazing Recommendation",
        "Feed Planning",
        "Decision Support"
    ]


def generate_summary(predictions):
    status, confidence = get_field_status(predictions)
    grazing = grazing_recommendation(predictions)
    feed_title, _ = feed_recommendation(predictions)
    interval = monitoring_interval(predictions)

    return f"""
            Field Status : {status}
            Prediction Confidence : {confidence}
            Recommended Action : {grazing['title']}
            Feed Planning : {feed_title}
            Monitoring : {interval}

            This recommendation is automatically generated from the
            predicted pasture biomass using the trained EfficientNet-B3
            multi-output regression model.

            """

def render_recommendations(predictions):
    st.subheader("AI Decision Support")
    grazing = grazing_recommendation(predictions)
    st.info(grazing["title"])
    st.write(grazing["message"])
    st.divider()

    feed_title, feed_msg = feed_recommendation(predictions)
    st.subheader("Feed Planning")
    st.success(feed_title)
    st.write(feed_msg)
    st.divider()

    st.subheader("Monitoring")
    st.write(monitoring_interval(predictions))
    st.divider()

    st.subheader("Estimated Time Savings")
    savings = estimate_savings()
    c1, c2, c3 = st.columns(3)

    c1.metric("Manual", savings["Manual Survey"])
    c2.metric("AI", savings["AI Prediction"])
    c3.metric("Saved", savings["Time Saved"])
    st.divider()

    st.subheader("Precision Agriculture")

    for item in precision_checklist():
        st.success(item)
    st.divider()

    st.subheader("AI Summary")
    st.code(generate_summary(predictions))