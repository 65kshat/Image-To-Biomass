import streamlit as st
import pandas as pd #type: ignore
from io import BytesIO
from datetime import datetime

from reportlab.lib import colors #type: ignore
from reportlab.lib.styles import getSampleStyleSheet #type: ignore
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle) #type: ignore

def prediction_dataframe(predictions):
    df = pd.DataFrame({"Biomass Type": list(predictions.keys()),
        "Predicted Value (g)": list(predictions.values())
    })

    return df


def report_information():
    return {
        "Project": "Image-to-Biomass Prediction System",
        "Model": "EfficientNet-B3",
        "Framework": "PyTorch", 
        "Frontend": "Streamlit",
        "Outputs": "5 Biomass Predictions",
        "Generated": datetime.now().strftime("%d-%m-%Y %H:%M")
    }


def generate_pdf_report(predictions, health_score, field_status, summary):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    elements = []
    elements.append(Paragraph("<b>Image-to-Biomass Prediction Report</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    info = report_information()

    for key, value in info.items():
        elements.append(Paragraph(f"<b>{key}</b>: {value}", styles["Normal"]))

    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Predicted Biomass Values</b>", styles["Heading2"]))

    table_data = [["Biomass Type", "Predicted Value (g)"]]

    for key, value in predictions.items():
        table_data.append([key, f"{value:.2f}"])
    table = Table(table_data)

    table.setStyle(
        TableStyle([
            ("BACKGROUND",(0,0),(-1,0),colors.green),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white),
            ("GRID",(0,0),(-1,-1),1,colors.black),
            ("BACKGROUND",(0,1),(-1,-1),colors.beige),
            ("BOTTOMPADDING",(0,0),(-1,0),8),
            ("ALIGN",(0,0),(-1,-1),"CENTER")
        ])
    )

    elements.append(table)
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Field Assessment</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Health Score : <b>{health_score:.1f}/100</b>", styles["Normal"]))
    elements.append(Paragraph(f"Field Status : <b>{field_status}</b>", styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AI Management Summary</b>", styles["Heading2"]))
    elements.append(Paragraph(summary.replace("\n", "<br/>"), styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Generated automatically using the Image-to-Biomass Prediction System.", styles["Italic"]))

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()

    return pdf

def download_report(pdf):
    st.download_button(
        label="Download AI Report",
        data=pdf,
        file_name="Biomass_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )