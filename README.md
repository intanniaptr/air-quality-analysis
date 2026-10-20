# Air Quality Analysis 🌫️

## Project Overview

This project focuses on exploratory data analysis (EDA) of Beijing air quality data collected from multiple monitoring stations between March 2013 and February 2017.

The analysis aims to explore air pollution patterns, compare pollutant concentrations across monitoring stations, and examine relationships between air quality variables. The findings are presented through an interactive dashboard built with Streamlit.

## Project Objectives

- Understand the characteristics and quality of the air quality dataset.
- Analyze changes in PM2.5 and PM10 concentrations over time.
- Compare average PM2.5 concentrations across monitoring stations.
- Explore relationships between air pollution variables.
- Communicate the results through data visualizations and an interactive dashboard.

## Dataset

The dataset contains air quality observations from 12 monitoring stations in Beijing, China, covering the period from March 2013 to February 2017.

| Attribute | Description |
|---|---|
| Location | Beijing, China |
| Observation period | March 2013 – February 2017 |
| Number of observations | 420,768 |
| Monitoring stations | 12 |
| Main variables analyzed | PM2.5 and PM10 |

The dataset files are stored in the `data/` directory. The dashboard uses `dashboard/main_data.csv`.

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

## Analysis Process

1. **Data Wrangling** — load, inspect, and prepare the dataset for analysis.
2. **Data Quality Assessment** — examine data types, missing values, and potential data quality issues.
3. **Data Cleaning** — handle data quality issues where appropriate and document the decisions made.
4. **Exploratory Data Analysis (EDA)** — investigate pollutant distributions, temporal patterns, station-level differences, and correlations.
5. **Data Visualization** — present important patterns through charts and statistical summaries.
6. **Dashboard Development** — build an interactive dashboard using Streamlit.

## Key Findings

The dashboard highlights the following observations:

- **Highest average PM2.5 concentration by station:** Dongsi, approximately 85.7 µg/m³.
- **Lowest average PM2.5 concentration by station:** Dingling, approximately 65.4 µg/m³.
- **Highest monthly average PM2.5:** December 2015, approximately 148.8 µg/m³.
- **Lowest monthly average PM2.5:** February 2016, approximately 42.9 µg/m³.
- **PM2.5 and PM10 correlation:** approximately 0.88, indicating a strong positive linear relationship in the analyzed data.

These findings describe the analyzed dataset and do not establish causal relationships.

## Interactive Dashboard

The dashboard includes:

- Summary statistics and key findings.
- Monthly air quality trends.
- Seasonal comparisons.
- Comparisons across monitoring stations.
- A correlation heatmap.
- A PM2.5 versus PM10 scatter plot.
- Relative PM2.5 concentration categories.
- A data table and CSV download functionality.

**Live Dashboard:**  
[Open Air Quality Analysis Dashboard](https://air-quality-analysis-4oux2y97vvycbml6ipcuwc.streamlit.app/)

## Project Structure

```text
Air_Quality_Analysis_Submission/
├── dashboard/
│   ├── dashboard.py
│   ├── main_data.csv
│   └── requirements.txt
├── data/
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv
│   ├── PRSA_Data_Changping_20130301-20170228.csv
│   ├── PRSA_Data_Dingling_20130301-20170228.csv
│   ├── PRSA_Data_Dongsi_20130301-20170228.csv
│   └── ... other monitoring station datasets
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Setup Environment

### Using Python Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

### Run the Streamlit Dashboard

Navigate to the dashboard directory:

```bash
cd dashboard
pip install -r requirements.txt
streamlit run dashboard.py
```

The dashboard will be available at the local URL displayed in the terminal, usually `http://localhost:8501`.

## Conclusion

This project demonstrates how exploratory data analysis and interactive visualization can be used to investigate air quality observations in Beijing. The analysis explores temporal patterns, differences across monitoring stations, and relationships between pollutant concentrations.

The interactive dashboard provides an accessible way to explore the data and review the findings.

---

*Developed as a data analysis project using Python, Jupyter Notebook, and Streamlit.*
