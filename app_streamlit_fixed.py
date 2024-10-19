
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib

# Set matplotlib backend to 'Agg' just in case
matplotlib.use('Agg')

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

# Plot PM2.5 Levels Over Time (using pandas plotting, no pyplot)
st.subheader('PM2.5 Levels Over Time')
pm25_plot = data_cleaned['PM2.5'].plot(figsize=(10, 6), title='PM2.5 Levels Over Time')
st.pyplot(pm25_plot.figure)

# Distribution of PM2.5 Categories using Seaborn
st.subheader('PM2.5 Levels Categorized')
sns_fig = sns.countplot(x='PM2.5_category', data=data_cleaned, palette='Set2')
sns_fig.set(title='Distribution of PM2.5 Levels by Category', xlabel='PM2.5 Category', ylabel='Count')
st.pyplot(sns_fig.figure)

# Correlation Between Temperature and PM2.5 (Seaborn scatter plot)
st.subheader('Correlation Between Temperature and PM2.5')
sns_fig_corr = sns.scatterplot(x='TEMP', y='PM2.5', data=data_cleaned)
sns_fig_corr.set(title='Correlation Between Temperature and PM2.5', xlabel='Temperature (°C)', ylabel='PM2.5 Concentration')
st.pyplot(sns_fig_corr.figure)
