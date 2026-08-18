# 🛰️ Satellite Telemetry Analyzer

A Python-based satellite telemetry analysis system designed to monitor
satellite health, analyze telemetry data, detect anomalies, and generate
mission reports and visualizations.

## 🚀 Features

- Satellite telemetry data processing
- Battery health monitoring
- Temperature monitoring
- Altitude monitoring
- Velocity monitoring
- Communication signal monitoring
- Overall satellite health assessment
- Rule-based anomaly detection
- Mission statistics
- Automated mission report generation
- Telemetry visualization
- Temperature anomaly visualization
- Altitude vs velocity relationship analysis

## 📊 Telemetry Parameters

The system analyzes:

- Battery (%)
- Temperature (°C)
- Altitude (km)
- Velocity (km/s)
- Signal strength

## 🚨 Anomaly Detection

The system detects abnormal telemetry conditions such as:

- Low battery
- High temperature
- Abnormal altitude
- Abnormal velocity
- Weak communication signal

## 📈 Visualizations

The project generates:

- Battery vs Time
- Temperature vs Time
- Altitude vs Time
- Velocity vs Time
- Altitude vs Velocity
- Temperature Anomaly Detection

## 📁 Project Structure

 Satellite-Telemetry-Analyzer/
│
├──  data/
│   └── 📄 telemetry.csv
│
├──  images/
│   ├──  battery_vs_time.png
│   ├── ️ temperature_vs_time.png
│   ├──  altitude_vs_time.png
│   ├──  velocity_vs_time.png
│   ├──  altitude_vs_velocity.png
│   └──  temperature_anomalies.png
│
├──  reports/
│   └──  mission_report.txt
│
├── 🐍 telemetry.py
├── 📖 README.md
├── 📦 requirements.txt
└── 🚫 .gitignore

## 🛠️ Technologies

- Python
- CSV
- Matplotlib

## ▶️ How to Run

Clone the repository and navigate into the project folder.

Install dependencies:

pip install -r requirements.txt

Run:

python telemetry.py

## 🎯 Project Goal

This project was developed to strengthen Python, data analysis,
visualization, and space-systems engineering concepts.

Future projects will explore machine learning and AI-based
satellite anomaly detection.

## 👨‍💻 Author

Syed Zain