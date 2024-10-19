
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Streamlit app content
st.title('Air Quality Dashboard - Tiantan Station')

# Show data
st.subheader('Dataset Preview')
st.write(data_cleaned.head())

# Plot PM2.5 Levels Over Time
st.subheader('PM2.5 Levels Over Time')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data_cleaned.index, data_cleaned['PM2.5'], label='PM2.5', color='blue')
ax.set_title('PM2.5 Levels Over Time', fontsize=14)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('PM2.5 Concentration', fontsize=12)
st.pyplot(fig)

# Distribution of PM2.5 Categories
st.subheader('PM2.5 Levels Categorized')
fig, ax = plt.subplots(figsize=(8, 6))
sns.countplot(x='PM2.5_category', data=data_cleaned, palette='Set2', ax=ax)
ax.set_title('Distribution of PM2.5 Levels by Category', fontsize=14)
ax.set_xlabel('PM2.5 Category', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
st.pyplot(fig)

# Correlation Between Temperature and PM2.5
st.subheader('Correlation Between Temperature and PM2.5')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='TEMP', y='PM2.5', data=data_cleaned, ax=ax)
ax.set_title('Correlation Between Temperature and PM2.5', fontsize=14)
ax.set_xlabel('Temperature (°C)', fontsize=12)
ax.set_ylabel('PM2.5 Concentration', fontsize=12)
st.pyplot(fig)
