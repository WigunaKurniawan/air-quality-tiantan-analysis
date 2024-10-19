
# Air Quality Analysis - Tiantan Station

This repository contains a data analysis project focused on air quality at the Tiantan Station. The analysis is based on a dataset spanning from March 2013 to February 2017. This project is submitted as part of the requirements for the Dicoding program and also serves as a data science portfolio.

## Project Overview
The goal of this project is to conduct an in-depth analysis of air quality at Tiantan Station, focusing on pollutants such as:

- **PM2.5** - Particulate matter with a diameter less than 2.5 micrometers.
- **PM10** - Particulate matter with a diameter less than 10 micrometers.
- **SO2** - Sulfur dioxide.
- **NO2** - Nitrogen dioxide.
- **CO** - Carbon monoxide.
- **O3** - Ozone.
- **Environmental factors** - Temperature, air pressure, wind speed, and precipitation.

## Business Questions
This analysis aims to answer the following business questions:

### Question 1: What are the trends of PM2.5 levels at Tiantan Station over the period from 2013 to 2017?
**Answer**: The analysis reveals that there are significant fluctuations in PM2.5 levels, with some seasonal peaks where pollution levels increase, particularly during the winter months.

### Question 2: Is there a correlation between temperature and PM2.5 levels?
**Answer**: A correlation analysis shows that as temperatures drop, PM2.5 levels tend to increase. This suggests that colder weather conditions might contribute to higher pollution levels, potentially due to increased heating activities and reduced dispersion of air pollutants.

### Additional Analysis - Binning for PM2.5 Levels
We conducted **binning analysis** for PM2.5 levels to categorize air quality into four groups:
- **Low**: PM2.5 < 35 µg/m³
- **Moderate**: 35 ≤ PM2.5 < 75 µg/m³
- **High**: 75 ≤ PM2.5 < 150 µg/m³
- **Very High**: PM2.5 > 150 µg/m³

This analysis helps identify the number of days with varying levels of air quality based on PM2.5 concentrations.

## Project Structure
```
air-quality-tiantan-analysis/
│
├── data/
│   └── PRSA_Data_Tiantan_20130301-20170228.csv   # Dataset used for analysis
├── app.py                                        # Streamlit app for interactive visualization
├── notebooks/
│   └── analysis_with_binning.ipynb               # Jupyter Notebook for detailed data analysis
├── README.md                                     # This readme file
├── requirements.txt                              # Python libraries required for the project
└── images/                                       # Folder for images used in README or Streamlit (optional)
```

## Technology Used
- **Python**: For data processing using `pandas`, `numpy`, and `matplotlib`.
- **Jupyter Notebook**: For detailed exploratory data analysis (EDA).
- **Streamlit**: For deploying an interactive dashboard in the cloud.
- **GitHub**: For version control and collaboration.

## How to Run the Project
### Clone the repository:
```
git clone https://github.com/WigunaKurniawan/air-quality-tiantan-analysis.git
```

### Install dependencies:
```
pip install -r requirements.txt
```
## How to Run the Dashboard

### Setup Environment - Anaconda
1. Create and activate a new environment with Python 3.9:
    ```bash
    conda create --name main-ds python=3.9
    conda activate main-ds
    pip install -r requirements.txt
    ```

### Setup Environment - Shell/Terminal
1. Create a project directory and navigate into it:
    ```bash
    mkdir proyek_analisis_data
    cd proyek_analisis_data
    ```
2. Install dependencies using pipenv:
    ```bash
    pipenv install
    pipenv shell
    pip install -r requirements.txt
    ```

### Run the Streamlit App
1. To run the dashboard, use the following command:
    ```bash
    streamlit run dashboard.py
    ```

This will start the Streamlit app, and you can access the interactive dashboard via your browser.


### Run the Streamlit app on the cloud:
- Go to [Streamlit Cloud](https://streamlit.io/cloud) and deploy the **app.py** from the GitHub repository for interactive visualization.

## License
This project is licensed under the **MIT License**. You are free to use and modify the code as long as appropriate credit is given.
