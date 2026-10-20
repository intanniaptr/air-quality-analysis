## Setup Environment - Anaconda

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit App

```bash
streamlit run dashboard.py
```

## Live Dashboard

Explore the deployed dashboard here:

[Air Quality Analysis Dashboard](https://air-quality-analysis-4oux2y97vvycbml6ipcuwc.streamlit.app/)
