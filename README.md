# 🌿 Image-to-Biomass Prediction System

> An AI-powered Deep Learning application for automated pasture biomass estimation, explainable AI visualization, and intelligent decision support.

---

## 📖 Overview

The **Image-to-Biomass Prediction System** is a computer vision application developed using **PyTorch**, **EfficientNet-B3**, and **Streamlit**. The system predicts multiple pasture biomass components directly from RGB field images, visualizes model attention using **Manual Grad-CAM**, and provides intelligent recommendations for grazing management and precision agriculture.

The project demonstrates the complete deployment of a Deep Learning regression model into an interactive web application with explainable AI and automated report generation.

---

# ✨ Features

## 🌿 Automated Biomass Estimation

Predicts five biomass components from a single RGB image:

- Dry Clover (g)
- Dry Dead (g)
- Dry Green (g)
- Dry Total (g)
- GDM (g)

---

## 🔥 Explainable AI

Manual Grad-CAM implementation provides visual explanations by highlighting image regions contributing most to each biomass prediction.

Features include:

- Heatmap Generation
- Overlay Visualization
- Target Selection
- Explainable Predictions

---

## 📊 Interactive Dashboard

The prediction dashboard includes:

- Biomass Prediction Cards
- Health Score
- Field Classification
- Bar Chart Visualization
- Pie Chart Visualization
- Prediction Statistics
- Prediction History

---

## 🌱 AI Decision Support

Automatically generates:

- Grazing Recommendations
- Feed Planning Suggestions
- Monitoring Schedule
- Field Health Assessment
- Precision Agriculture Checklist
- AI-generated Management Summary

---

## 📄 Automated Report Generation

Generate downloadable PDF reports containing:

- Biomass Predictions
- Field Health Status
- AI Recommendations
- Project Information
- Assessment Summary

---

# 🧠 Deep Learning Model

| Component | Details |
|-----------|---------|
| Model | EfficientNet-B3 |
| Framework | PyTorch |
| Learning Type | Transfer Learning |
| Task | Multi-Output Image Regression |
| Outputs | 5 Biomass Predictions |
| Explainability | Manual Grad-CAM |

---

# 🛠 Technologies Used

## Artificial Intelligence

- PyTorch
- TorchVision
- EfficientNet-B3
- Transfer Learning
- Manual Grad-CAM

## Data Processing

- NumPy
- Pandas
- OpenCV
- Pillow

## Visualization

- Matplotlib
- Streamlit

## Report Generation

- ReportLab

---

# 📂 Project Structure

```text
Image-to-Biomass-Prediction-System
│
├── Dataset/
├── Frontend/
│   ├── app.py
│   ├── Home.py
│   ├── Prediction.py
│   └── Insights.py
│
├── Models/
│   └── best_model.pth
│
├── Notebooks/
│
├── Outputs/
│
├── Utils/
│   ├── ModelUtils.py
│   ├── DashboardUtils.py
│   ├── RecommendationUtils.py
│   └── ReportUtils.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Expected Outcomes

- ✅ Automated biomass estimation from field images
- ✅ Explainable AI using Manual Grad-CAM
- ✅ Interactive prediction dashboard
- ✅ AI-assisted grazing recommendations
- ✅ Feed planning support
- ✅ Precision agriculture support
- ✅ Automated PDF report generation
- ✅ Reduced manual field survey effort

---

# 🚀 Installation

Clone the repository

```bash
git clone YOUR_GITHUB_LINK
```

Navigate to the project

```bash
cd Image-to-Biomass-Prediction-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch the application

```bash
streamlit run Frontend/app.py
```

---

# 📷 Dataset

> **Note:** The dataset is **not included** in this repository due to its size and distribution restrictions.

Download the dataset from:

**Dataset Link:**

```
PASTE_DATASET_LINK_HERE
```

After downloading, place the dataset inside the project directory as follows:

```text
Dataset/
│
├── train/
├── test/
├── train.csv
└── test.csv
```

---

# 🖥 Application Workflow

```text
Upload RGB Image
        │
        ▼
Image Preprocessing
        │
        ▼
EfficientNet-B3 Prediction
        │
        ▼
Biomass Estimation
        │
        ▼
AI Dashboard
        │
        ▼
Manual Grad-CAM
        │
        ▼
Decision Support
        │
        ▼
Generate PDF Report
```

---

# 📈 Future Improvements

Potential future enhancements include:

- Real-time Drone Monitoring
- Live Camera Integration
- GPS-based Field Mapping
- Satellite Image Support
- Weather API Integration
- IoT Sensor Connectivity
- Cloud Deployment
- Mobile Application

---

# 👨‍💻 Author

**Akshat Sohni**

Artificial Intelligence & Data Science Engineering

---

# 📜 License

This project was developed for educational and research purposes.
