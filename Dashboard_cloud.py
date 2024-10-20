import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the app title
st.title('Air Quality Analysis at Tiantan Station (2013-2017)')
st.write("""
**Author**: Wiguna Kurniawan  
**Email**: [wiguna_kurniawan@ymail.com](mailto:wiguna_kurniawan@ymail.com)  
**Dicoding ID**: Wiguna Kurniawan

This project focuses on analyzing air quality data at Tiantan Station, specifically trends in pollutants like PM2.5 and correlations with environmental factors such as temperature.
""")

# Project Overview
st.header('Project Overview')
st.write("""
The primary goal is to explore trends in various pollutants including:
- **PM2.5**: Fine particulate matter
- **PM10**: Particulate matter
- **SO2**: Sulfur dioxide
- **NO2**: Nitrogen dioxide
- **CO**: Carbon monoxide
- **O3**: Ozone
- **Environmental Factors**: Temperature, air pressure, wind speed, and precipitation
""")

# Business Questions
st.subheader('Business Questions')
st.write("""
1. What are the trends of PM2.5 levels at Tiantan Station from 2013 to 2017?  
2. Is there a correlation between temperature and PM2.5 levels?
""")

# Load Data
st.header('Data Loading')
data_url = 'https://raw.githubusercontent.com/WigunaKurniawan/air-quality-tiantan-analysis/main/Dashboard/PRSA_Data_Tiantan_20130301-20170228.csv'
data = pd.read_csv(data_url)

st.write('Preview of the dataset:')
st.write(data.head())

# Data Wrangling
st.header('Data Wrangling')
st.write("""
Handling missing values and creating a datetime index for easier time-based analysis.
""")
data['datetime'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])
data.set_index('datetime', inplace=True)
data_cleaned = data.fillna(method='ffill')
st.write('Preview of cleaned data:')
st.write(data_cleaned.head())

# PM2.5 Trends Over Time
st.header('PM2.5 Trends Over Time')
monthly_pm25 = data_cleaned['PM2.5'].resample('M').mean()

plt.figure(figsize=(10, 6))
plt.plot(monthly_pm25.index, monthly_pm25, label='PM2.5 (Monthly Avg)', color='royalblue', linewidth=2, marker='o')
plt.title('Monthly Average PM2.5 Levels (2013-2017)', fontsize=14)
plt.xlabel('Date (Month-Year)', fontsize=12)
plt.ylabel('PM2.5 Concentration (µg/m³)', fontsize=12)
plt.grid(True)
plt.legend(loc='upper right')
st.pyplot(plt)

# Correlation Between PM2.5 and Temperature
st.header('Correlation Between PM2.5 and Temperature')
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

# Heatmap Correlation Matrix
st.subheader('Correlation Heatmap')
correlation_matrix = data_cleaned[['PM2.5', 'TEMP']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1, square=True)
plt.title('Correlation Between PM2.5 and Temperature', fontsize=14, pad=12)
st.pyplot(plt)

# Conclusion
st.header('Conclusion')
st.write("""
- PM2.5 levels fluctuated with peaks in early 2014 and late 2015 to early 2016.
- There is no clear long-term downward trend in PM2.5 levels.
- Temperature does not appear to significantly impact PM2.5 levels based on weak correlation.
- Recommendations include implementing year-round pollution control, promoting clean energy, and raising public awareness about air quality.
""")
