import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the app title and structure
st.title('Air Quality Analysis at Tiantan Station (2013-2017)')

# Section 1: Introduction
st.header('Introduction')
st.write("""
This project analyzes the air quality data at Tiantan Station from 2013 to 2017.
We explore the trends of pollutants, particularly PM2.5, and their correlation with temperature.

**Author**: Wiguna Kurniawan  
**Email**: [wiguna_kurniawan@ymail.com](mailto:wiguna_kurniawan@ymail.com)
""")

# Section 2: Business Questions
st.header('Business Questions')
st.write("""
1. What are the trends of PM2.5 levels at Tiantan Station from 2013 to 2017?
2. Is there a correlation between temperature and PM2.5 levels?
""")

# Section 3: Data Loading
st.header('Data Loading')
data_url = 'https://raw.githubusercontent.com/WigunaKurniawan/air-quality-tiantan-analysis/main/Dashboard/PRSA_Data_Tiantan_20130301-20170228.csv'
data = pd.read_csv(data_url)

st.write("Here is a preview of the dataset:")
st.write(data.head())

# Section 4: Data Wrangling
st.header('Data Wrangling')
st.write("""
We will now clean the data, handle missing values, and create a 'datetime' column to facilitate time series analysis.
""")
data['datetime'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])
data.set_index('datetime', inplace=True)
data_cleaned = data.fillna(method='ffill')  # Forward fill missing values

st.write('Here is the cleaned dataset:')
st.write(data_cleaned.head())

# Section 5: Exploratory Data Analysis (EDA)
st.header('Exploratory Data Analysis')

# PM2.5 Trends Visualization
st.subheader('PM2.5 Trends Over Time (Monthly Averages)')
monthly_pm25 = data_cleaned['PM2.5'].resample('M').mean()

plt.figure(figsize=(10, 6))
plt.plot(monthly_pm25.index, monthly_pm25, label='PM2.5 (Monthly Avg)', color='royalblue', linewidth=2, marker='o')
plt.title('PM2.5 Levels Over Time (2013-2017)', fontsize=14)
plt.xlabel('Date (Month-Year)', fontsize=12)
plt.ylabel('PM2.5 Concentration (µg/m³)', fontsize=12)
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

# Correlation Between PM2.5 and Temperature (Heatmap)
st.subheader('Correlation Between PM2.5 and Temperature')
annual_data = data_cleaned[['PM2.5', 'TEMP']].resample('Y').mean()
correlation_matrix = annual_data.corr()

plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1, square=True)
plt.title('Annual Correlation Between PM2.5 and Temperature (2013-2017)', fontsize=14)
plt.tight_layout()
st.pyplot(plt)

# Section 6: Annual Trends of PM2.5 and Temperature
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

# Section 7: Conclusion
st.header('Conclusion')
st.write("""
- **PM2.5 Trends**: There are noticeable spikes in PM2.5 levels, particularly in 2014 and 2016. There is no clear downward trend.
- **Correlation**: The correlation between temperature and PM2.5 levels is weak, implying that other factors influence PM2.5 levels.
- **Recommendations**: To reduce PM2.5 levels, it is recommended to implement consistent pollution control measures, particularly during periods of high pollution.
""")
