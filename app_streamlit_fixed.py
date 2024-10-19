
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title and Introduction
st.title('Air Quality Analysis - Tiantan Station')
st.markdown('''
This dashboard presents an analysis of air quality data collected from the **Tiantan Station** for the period between **2013 and 2017**.
The primary focus is on understanding the levels of **PM2.5** and their relationship with environmental factors like temperature.

---

## Business Questions Addressed:
1. **What are the trends of PM2.5 levels at Tiantan Station over the period from 2013 to 2017?**
2. **Is there a correlation between temperature and PM2.5 levels?**
''')

# Load the dataset
data_url = 'https://raw.githubusercontent.com/WigunaKurniawan/air-quality-tiantan-analysis/main/Dataset/PRSA_Data_Tiantan_20130301-20170228.csv'
data = pd.read_csv(data_url)

# Data Cleaning and Wrangling
data_cleaned = data.fillna(method='ffill')
data_cleaned['datetime'] = pd.to_datetime(data_cleaned[['year', 'month', 'day', 'hour']])
data_cleaned.set_index('datetime', inplace=True)

# Binning PM2.5 levels into categories
def categorize_pm25(value):
    if value < 35:
        return 'Low'
    elif 35 <= value < 75:
        return 'Moderate'
    elif 75 <= value < 150:
        return 'High'
    else:
        return 'Very High'

# Apply the binning function
data_cleaned['PM2.5_category'] = data_cleaned['PM2.5'].apply(categorize_pm25)

# Show Data Preview
st.subheader('Dataset Preview')
st.write(data_cleaned.head())

# PM2.5 Levels Over Time
st.markdown('### PM2.5 Levels Over Time')
st.markdown('This plot shows how PM2.5 levels fluctuate throughout the analyzed period.')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data_cleaned.index, data_cleaned['PM2.5'], label='PM2.5', color='blue')
ax.set_title('PM2.5 Levels Over Time at Tiantan Station', fontsize=14)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('PM2.5 Concentration', fontsize=12)
st.pyplot(fig)

# Distribution of PM2.5 Categories
st.markdown('### PM2.5 Levels Categorized')
st.markdown('This bar chart categorizes the PM2.5 levels into Low, Moderate, High, and Very High categories.')
fig, ax = plt.subplots(figsize=(8, 6))
sns.countplot(x='PM2.5_category', data=data_cleaned, palette='Set2', ax=ax)
ax.set_title('Distribution of PM2.5 Levels by Category', fontsize=14)
ax.set_xlabel('PM2.5 Category', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
st.pyplot(fig)

# Correlation Between Temperature and PM2.5
st.markdown('### Correlation Between Temperature and PM2.5')
st.markdown('This scatter plot illustrates the correlation between temperature and PM2.5 levels.')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='TEMP', y='PM2.5', data=data_cleaned, ax=ax)
ax.set_title('Correlation Between Temperature and PM2.5', fontsize=14)
ax.set_xlabel('Temperature (°C)', fontsize=12)
ax.set_ylabel('PM2.5 Concentration', fontsize=12)
st.pyplot(fig)

# Conclusion Section
st.markdown('''
---

## Conclusion:
1. **PM2.5 levels show significant seasonal variation**, with higher levels during colder months.
2. **Negative correlation between temperature and PM2.5**: Lower temperatures are associated with higher PM2.5 levels, likely due to increased heating activities and reduced air dispersion during cold weather.

This analysis helps identify potential interventions to improve air quality, especially during colder months.
''')
