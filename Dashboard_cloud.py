import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title and Author Information
st.title('Air Quality Analysis at Tiantan Station (2013-2017)')
st.write("""
**Author**: Wiguna Kurniawan  
**Email**: [wiguna_kurniawan@ymail.com](mailto:wiguna_kurniawan@ymail.com)  
**Dicoding ID**: Wiguna Kurniawan
""")

# Project Overview
st.header('Project Overview')
st.subheader('Business Questions')
st.write("""
1. What are the trends of PM2.5 levels at Tiantan Station from 2013 to 2017?  
2. Is there a correlation between temperature and PM2.5 levels?
3. What are the distributions of air quality metrics such as PM2.5, PM10, NO2, and CO?
4. How do air quality indicators correlate with each other and with meteorological factors?
""")

# Load the dataset
st.subheader('Load the Air Quality Dataset')
data_url = 'https://raw.githubusercontent.com/WigunaKurniawan/air-quality-tiantan-analysis/main/Dashboard/PRSA_Data_Tiantan_20130301-20170228.csv'
data = pd.read_csv(data_url)
st.write('Preview of the dataset:')
st.write(data.head())

# Data Wrangling Section
st.header('Data Wrangling')

st.subheader('Gathering Data')
st.write("We will gather the dataset, which includes air quality measurements for pollutants and environmental factors.")

# Missing Data Analysis
st.subheader('Assessing Data')
st.write("Checking for missing values and ensuring data quality.")
missing_values = data.isnull().sum()
st.write('Missing values in the dataset:')
st.write(missing_values)

# Cleaning the data by handling missing values
st.subheader('Cleaning Data')
st.write("""
Missing values will be handled using forward fill, and a datetime index will be created.
""")
data['datetime'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])
data.set_index('datetime', inplace=True)
data_cleaned = data.fillna(method='ffill')
st.write('Preview of cleaned data:')
st.write(data_cleaned.head())

# Summary Statistics
st.subheader('Summary Statistics')
st.write("Below are the summary statistics for the numerical variables in the dataset:")
st.write(data_cleaned.describe())

# Exploratory Data Analysis (EDA)
st.header('Exploratory Data Analysis (EDA)')

# PM2.5 trends over time
st.subheader('Explore PM2.5 Trends Over Time')
monthly_pm25 = data_cleaned['PM2.5'].resample('M').mean()
plt.figure(figsize=(10, 6))
plt.plot(monthly_pm25.index, monthly_pm25, label='PM2.5 (Monthly Avg)', color='royalblue', linewidth=2, marker='o')
plt.title('Monthly Average PM2.5 Levels (2013-2017)', fontsize=14)
plt.xlabel('Date (Month-Year)', fontsize=12)
plt.ylabel('PM2.5 Concentration (µg/m³)', fontsize=12)
plt.grid(True)
plt.legend(loc='upper right')
st.pyplot(plt)

# Correlation between PM2.5 and Temperature
st.subheader('Explore Correlation Between PM2.5 and Temperature')
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

# Distribution of Air Quality Metrics
st.subheader('Distribution of Air Quality Metrics')
st.write('Visualizing the distributions of PM2.5, PM10, NO2, and CO concentrations.')

# Plot distributions for PM2.5, PM10, NO2, and CO
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.histplot(data_cleaned['PM2.5'].dropna(), bins=50, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('PM2.5 Distribution')

sns.histplot(data_cleaned['PM10'].dropna(), bins=50, kde=True, ax=axes[0, 1])
axes[0, 1].set_title('PM10 Distribution')

sns.histplot(data_cleaned['NO2'].dropna(), bins=50, kde=True, ax=axes[1, 0])
axes[1, 0].set_title('NO2 Distribution')

sns.histplot(data_cleaned['CO'].dropna(), bins=50, kde=True, ax=axes[1, 1])
axes[1, 1].set_title('CO Distribution')

plt.tight_layout()
st.pyplot(fig)

# Correlation Matrix Analysis
st.subheader('Correlation Matrix of Air Quality Indicators and Meteorological Variables')
st.write('We will now analyze correlations between air quality indicators (PM2.5, PM10, SO2, NO2, CO, etc.) and meteorological variables (TEMP, PRES, WSPM).')

# Calculate the correlation matrix
corr_matrix = data_cleaned[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'WSPM']].corr()

# Heatmap for correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Air Quality and Meteorological Variables')
st.pyplot(plt)

# Visualization & Explanatory Analysis
st.header('Visualization & Explanatory Analysis')

st.subheader('Question 1: What are the trends of PM2.5 levels?')
st.write("""
The trends of PM2.5 levels at Tiantan Station from 2013 to 2017 show fluctuating patterns with peaks in early 2014 and late 2015 to early 2016. There is no clear long-term downward trend, indicating that high levels of pollution persisted throughout the period.
""")

# Correlation Heatmap
st.subheader('Question 2: Is there a correlation between temperature and PM2.5 levels?')
correlation_matrix_temp = data_cleaned[['PM2.5', 'TEMP']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix_temp, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1, square=True)
plt.title('Correlation Between PM2.5 and Temperature', fontsize=14, pad=12)
st.pyplot(plt)
st.write("""
The correlation between temperature and PM2.5 levels is weak, suggesting temperature has little direct influence on PM2.5 concentration.
""")

# Conclusion
st.header('Conclusion')
st.write("""
1. **PM2.5 Trends**: PM2.5 levels fluctuated significantly from 2013 to 2017 with no consistent downward trend.
2. **Correlation**: Temperature does not appear to significantly impact PM2.5 levels based on the weak correlation observed.
3. **Recommendations**: Pollution control measures should be implemented year-round, especially during high pollution periods, along with promoting clean energy.
""")
