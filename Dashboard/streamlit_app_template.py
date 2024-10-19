
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title and Introduction
st.title('Air Quality Data Analysis - Tiantan Station')
st.markdown('''
This dashboard presents a full analysis of air quality data collected from the **Tiantan Station** for the period between **2013 and 2017**.

**Nama**: Wiguna Kurniawan  
**Email**: wiguna_kurniawan@ymail.com  
**ID Dicoding**: Wiguna Kurniawan

---

We will conduct the following steps:

- Data Loading
- Data Cleaning and Wrangling
- Exploratory Data Analysis (EDA)
- Binning Analysis
- Conclusion

---
''')

# Step 2: Load the Air Quality Dataset
st.subheader('Step 2: Load the Air Quality Dataset')
st.markdown("We will load the dataset directly from the GitHub link to perform the analysis. The dataset is already combined into a single CSV file.")

# Load the dataset
data_url = 'https://raw.githubusercontent.com/WigunaKurniawan/air-quality-tiantan-analysis/main/Dataset/PRSA_Data_Tiantan_20130301-20170228.csv'
data = pd.read_csv(data_url)

# Display the first few rows
st.write(data.head())

# Step 3: Data Cleaning
st.subheader('Step 3: Data Cleaning')
st.markdown('''We will check for missing values and handle them using the forward fill method.
Additionally, we will create a datetime column using the year, month, day, and hour columns.''')

# Handle missing values with forward fill
data_cleaned = data.fillna(method='ffill')

# Create datetime column for easier analysis
data_cleaned['datetime'] = pd.to_datetime(data_cleaned[['year', 'month', 'day', 'hour']])
data_cleaned.set_index('datetime', inplace=True)

# Verify if there are still missing values
st.write(data_cleaned.isnull().sum())

# Step 4: Exploratory Data Analysis (EDA)
st.subheader('Step 4: Exploratory Data Analysis (EDA)')
st.markdown("In this section, we will perform visualizations to explore trends in PM2.5 levels and analyze correlations between temperature and PM2.5.")

# Plot PM2.5 levels over time
st.markdown("### PM2.5 Levels Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data_cleaned.index, data_cleaned['PM2.5'], label='PM2.5', color='blue')
ax.set_title('PM2.5 Levels Over Time at Tiantan Station', fontsize=14)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('PM2.5 Concentration', fontsize=12)
st.pyplot(fig)

# Correlation between temperature and PM2.5
st.markdown("### Correlation Between Temperature and PM2.5 Levels")
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='TEMP', y='PM2.5', data=data_cleaned, ax=ax)
ax.set_title('Correlation between Temperature and PM2.5 Levels', fontsize=14)
ax.set_xlabel('Temperature (°C)', fontsize=12)
ax.set_ylabel('PM2.5 Concentration', fontsize=12)
st.pyplot(fig)

# Step 5: Binning Analysis for PM2.5 Levels
st.subheader('Step 5: Binning Analysis for PM2.5 Levels')
st.markdown('''We will classify PM2.5 levels into categories such as 'Low', 'Moderate', 'High', and 'Very High'.''')

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

# Apply the binning function to the 'PM2.5' column
data_cleaned['PM2.5_category'] = data_cleaned['PM2.5'].apply(categorize_pm25)

# Check the distribution of categories
category_counts = data_cleaned['PM2.5_category'].value_counts()
st.write(category_counts)

# Visualize the distribution of PM2.5 categories
st.markdown("### Distribution of PM2.5 Levels by Category")
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x='PM2.5_category', data=data_cleaned, palette='Set2', ax=ax)
ax.set_title('Distribution of PM2.5 Levels by Category', fontsize=14)
ax.set_xlabel('PM2.5 Category', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
st.pyplot(fig)

# Step 6: Conclusion
st.subheader('Step 6: Conclusion')
st.markdown('''
- **PM2.5 levels show significant seasonal variation**, with higher levels during colder months.
- **Negative correlation between temperature and PM2.5** suggests that colder weather conditions lead to higher pollution levels.
- Binning analysis indicates that the majority of days fall into the 'Moderate' and 'High' categories for PM2.5 levels.
''')
