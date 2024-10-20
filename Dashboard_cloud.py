import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title('Air Quality Analysis at Tiantan Station (2013-2017)')

# Introduction
st.header('Introduction')
st.write("""
This is an in-depth analysis of air quality at Tiantan Station for the period from 2013 to 2017. 
We will explore pollutants such as PM2.5, PM10, SO2, and their relationships with environmental factors like temperature.
\n\n**Author**: Wiguna Kurniawan  
**Email**: [wiguna_kurniawan@ymail.com](mailto:wiguna_kurniawan@ymail.com)  
**Dicoding ID**: Wiguna Kurniawan
""")

# Business Questions
st.header('Business Questions')
st.write("""
The key business questions we aim to answer are:
1. What are the trends of PM2.5 levels at Tiantan Station over the period from 2013 to 2017?
2. Is there a correlation between temperature and PM2.5 levels?
""")

# Data Loading Section
st.header('Data Loading')
data_url = 'https://raw.githubusercontent.com/WigunaKurniawan/air-quality-tiantan-analysis/main/Dashboard/PRSA_Data_Tiantan_20130301-20170228.csv'
data = pd.read_csv(data_url)
st.write('Dataset preview:')
st.write(data.head())

# Data Wrangling Section
st.header('Data Wrangling')
st.write("""
We will handle missing values and create a new datetime column for easier analysis. 
We will also forward-fill missing values to maintain the continuity of time series data.
""")
data['datetime'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])
data.set_index('datetime', inplace=True)
data_cleaned = data.fillna(method='ffill')
st.write('Data after wrangling (first few rows):')
st.write(data_cleaned.head())

# PM2.5 Trends Section
st.header('PM2.5 Trends Over Time')
st.write("The following plot shows the monthly average PM2.5 levels from 2013 to 2017.")
monthly_pm25 = data_cleaned['PM2.5'].resample('M').mean()
plt.figure(figsize=(10, 6))
plt.plot(monthly_pm25.index, monthly_pm25, label='PM2.5 (Monthly Avg)', color='royalblue', linewidth=2, marker='o')
plt.title('PM2.5 Levels Over Time at Tiantan Station (2013-2017)', fontsize=14)
plt.xlabel('Date (Month-Year)', fontsize=12)
plt.ylabel('PM2.5 Concentration (µg/m³)', fontsize=12)
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

# Correlation Between PM2.5 and Temperature
st.header('Correlation Between PM2.5 and Temperature')
st.write("Below is a correlation heatmap showing the relationship between PM2.5 and Temperature.")
annual_data = data_cleaned[['PM2.5', 'TEMP']].resample('Y').mean()
correlation_matrix = annual_data.corr()
plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1, square=True)
plt.title('Annual Correlation Matrix: PM2.5 and Temperature (2013-2017)', fontsize=14)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
st.pyplot(plt)

# Annual Trends of PM2.5 and Temperature
st.header('Annual Trends of PM2.5 and Temperature')
annual_pm25 = data_cleaned['PM2.5'].resample('Y').mean()
annual_temp = data_cleaned['TEMP'].resample('Y').mean()
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(annual_pm25.index, annual_pm25, color='blue', marker='o', linewidth=2, label='PM2.5 (Annual Avg)')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('PM2.5 Concentration (µg/m³)', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True)
ax2 = ax1.twinx()
ax2.plot(annual_temp.index, annual_temp, color='red', marker='o', linewidth=2, label='Temperature (Annual Avg)')
ax2.set_ylabel('Temperature (°C)', fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')
plt.title('Annual Trends of PM2.5 and Temperature (2013-2017)', fontsize=14, pad=15)
fig.tight_layout()
st.pyplot(fig)

# Conclusion Section
st.header('Conclusion')
st.write("""
- PM2.5 levels show significant fluctuations over the years, with peaks around 2014 and 2016. There is no clear downward trend in pollution levels.
- There is a weak correlation between PM2.5 and temperature, suggesting that other factors are more influential in PM2.5 concentrations.
- Recommendations include year-round pollution control measures, promoting clean energy, and raising public awareness to mitigate pollution.
""")
