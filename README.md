# Air Quality Analysis Dashboard

An exploratory data analysis project focused on Beijing air quality data from 2013 to 2017. This project explores air pollution patterns, compares particulate matter concentrations across monitoring stations, and presents the findings through an interactive dashboard built with Streamlit.

## Live Dashboard

**Explore the dashboard here:**  
[Air Quality Analysis Dashboard](https://air-quality-analysis-4oux2y97vvycbml6ipcuwc.streamlit.app/)

## Project Overview

Air pollution is an important environmental issue that can affect public health and quality of life. Analyzing air quality data helps identify pollution patterns, compare monitoring locations, and understand changes in pollutant concentrations over time.

This project uses exploratory data analysis (EDA) to investigate Beijing air quality measurements and presents key findings through an interactive dashboard.

## Objectives

- Explore air quality data and understand its characteristics.
- Examine trends in PM2.5 and PM10 concentrations over time.
- Compare air quality measurements across monitoring stations.
- Investigate relationships between selected air pollution variables.
- Present analytical findings through an interactive dashboard.

## Dataset

The dataset contains air quality observations collected from Beijing monitoring stations.

| Attribute | Description |
|---|---|
| Location | Beijing, China |
| Period | March 2013 – February 2017 |
| Observations | 420,768 rows |
| Monitoring stations | 12 stations |
| Main variables of interest | PM2.5 and PM10 |

The dataset contains measurements from multiple monitoring stations and is used to explore temporal patterns, station-level differences, and relationships between air pollution variables.

## Tools and Technologies

- **Python** — data analysis and processing
- **Pandas** — data manipulation
- **NumPy** — numerical operations
- **Matplotlib and Seaborn** — data visualization, where applicable
- **Plotly** — interactive visualizations
- **Streamlit** — interactive dashboard
- **Jupyter Notebook** — exploratory data analysis

## Analysis Workflow

1. **Data Loading** — load the dataset and inspect its structure.
2. **Data Understanding** — examine dimensions, data types, descriptive statistics, and variable distributions.
3. **Data Cleaning** — inspect missing values, data quality issues, and potential outliers.
4. **Exploratory Data Analysis** — investigate air quality trends, station-level differences, and correlations.
5. **Visualization** — create charts to communicate the analysis results.
6. **Dashboard Development** — build an interactive dashboard using Streamlit.
7. **Deployment** — publish the dashboard using Streamlit Community Cloud.

## Key Findings

The dashboard highlights the following findings from the analysis:

- **Highest average PM2.5:** Dongsi, approximately 85.7 µg/m³.
- **Lowest average PM2.5:** Dingling, approximately 65.4 µg/m³.
- **Highest monthly average PM2.5:** December 2015, approximately 148.8 µg/m³.
- **Lowest monthly average PM2.5:** February 2016, approximately 42.9 µg/m³.
- **PM2.5 and PM10 correlation:** approximately 0.88, indicating a strong positive linear relationship in the analyzed data.

These findings describe the dataset and should not be interpreted as proof of causation.

## Dashboard Features

- Summary statistics and key performance indicators.
- Key findings highlighting important observations.
- Monthly air quality trends.
- Seasonal comparisons.
- Air quality comparisons across monitoring stations.
- Correlation heatmap.
- PM2.5 and PM10 scatter plot.
- PM2.5 concentration categories based on relative tertiles.
- Data table and CSV download functionality.

## Repository Structure

```text
air-quality-analysis/
├── dashboard.py
├── main_data.csv
├── requirements.txt
├── README.md
└── .gitignore
```

The repository structure above represents the deployed dashboard project. The analysis notebook and any additional submission files may be maintained separately.

## Run the Dashboard Locally

### 1. Clone the repository

```bash
git clone https://github.com/intanniaptr/air-quality-analysis.git
cd air-quality-analysis
```

### 2. Create and activate a virtual environment (optional but recommended)

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run dashboard.py
```

The dashboard will be available at the local URL displayed in your terminal, usually `http://localhost:8501`.

## Deployment

The dashboard is deployed using **Streamlit Community Cloud** and can be accessed here:

[Open the live dashboard](https://air-quality-analysis-4oux2y97vvycbml6ipcuwc.streamlit.app/)

## Conclusion

This project demonstrates how exploratory data analysis and interactive visualization can be used to investigate air quality data. By examining pollutant trends, comparing monitoring stations, and exploring relationships between variables, the dashboard provides an accessible way to explore Beijing's air quality observations.

---

*Developed as a data analysis project using Python and Streamlit.*
