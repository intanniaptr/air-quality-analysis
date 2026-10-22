# Air Quality Analysis 🌫️

## Project Overview

This project focuses on exploratory data analysis (EDA) of Beijing air quality data collected from multiple monitoring stations between March 2013 and February 2017.

The project aims to explore air pollution patterns, compare pollutant concentrations across monitoring stations, and investigate relationships between air quality variables. The findings are presented through an interactive dashboard developed using Streamlit.

## Project Objectives

- Understand the characteristics and quality of the air quality dataset.
- Analyze changes in PM2.5 and PM10 concentrations over time.
- Compare average PM2.5 concentrations across monitoring stations.
- Explore relationships between air pollution variables.
- Communicate analytical findings through data visualizations and an interactive dashboard.

## Dataset

The dataset contains air quality observations from 12 monitoring stations in Beijing, China, covering the period from March 2013 to February 2017.

| Attribute | Description |
|---|---|
| Location | Beijing, China |
| Observation Period | March 2013 – February 2017 |
| Number of Observations | 420,768 |
| Monitoring Stations | 12 |
| Main Variables Analyzed | PM2.5 and PM10 |

The original station-level datasets are stored in the `data/` directory. The dashboard uses the processed dataset available at `dashboard/main_data.csv`.

## Tools and Libraries

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn, Plotly
- **Dashboard Development:** Streamlit
- **Development Environment:** Jupyter Notebook

## Analysis Process

1. **Data Wrangling** — Load, inspect, and prepare the dataset for analysis.
2. **Data Quality Assessment** — Examine data types, missing values, and potential data quality issues.
3. **Data Cleaning** — Address data quality issues where appropriate and document the decisions made.
4. **Exploratory Data Analysis (EDA)** — Investigate pollutant distributions, temporal patterns, station-level differences, and correlations.
5. **Data Visualization** — Present important patterns through charts and statistical summaries.
6. **Dashboard Development** — Develop an interactive dashboard using Streamlit.

## Key Findings

The analysis highlights the following observations:

- **Highest Average PM2.5 by Station:** Dongsi, approximately 85.7 µg/m³.
- **Lowest Average PM2.5 by Station:** Dingling, approximately 65.4 µg/m³.
- **Highest Monthly Average PM2.5:** December 2015, approximately 148.8 µg/m³.
- **Lowest Monthly Average PM2.5:** February 2016, approximately 42.9 µg/m³.
- **PM2.5 and PM10 Correlation:** Approximately 0.88, indicating a strong positive linear relationship in the analyzed data.

These findings describe the analyzed dataset and do not establish causal relationships.

*Note: The reported values should be consistent with the calculations and filters used in the notebook and dashboard.*

## Interactive Dashboard

The interactive dashboard allows users to explore air quality data through the following features:

- Summary statistics and key findings.
- Monthly air quality trends.
- Seasonal comparisons.
- Comparisons across monitoring stations.
- A correlation heatmap.
- A PM2.5 versus PM10 scatter plot.
- Relative PM2.5 concentration categories.
- An interactive data table and CSV download functionality.

**Live Dashboard:** [Open Air Quality Analysis Dashboard](https://air-quality-analysis-4oux2y97vvycbml6ipcuwc.streamlit.app/)

## Project Structure

```text
Air_Quality_Analysis_Submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv
│   ├── PRSA_Data_Changping_20130301-20170228.csv
│   ├── PRSA_Data_Dingling_20130301-20170228.csv
│   ├── PRSA_Data_Dongsi_20130301-20170228.csv
│   └── ... other monitoring station datasets
├── notebook.ipynb
├── requirements.txt
├── README.md
└── url.txt
```

## Setup and Installation

### Prerequisites

- Python 3 installed on your system.
- Git installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/intanniaptr/air-quality-analysis.git
cd air-quality-analysis
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate the virtual environment.

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Dashboard

From the repository root directory, execute:

```bash
streamlit run dashboard/dashboard.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Conclusion

This project demonstrates how exploratory data analysis and interactive visualization can be used to investigate air quality observations in Beijing. By examining temporal patterns, differences across monitoring stations, and relationships between pollutant concentrations, the project provides an interactive way to explore air quality data and review analytical findings.

---

*Developed as a data analysis project using Python, Jupyter Notebook, and Streamlit.*
