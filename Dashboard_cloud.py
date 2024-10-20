import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
st.title('Air Quality Data Dashboard')

st.write("""
## Summary Statistics and Exploratory Data Analysis (EDA)
In this dashboard, we will explore trends in air quality levels and analyze various correlations between variables like PM2.5, PM10, and meteorological factors such as temperature and wind speed.
""")

# Load the data
@st.cache
def load_data():
    data = pd.read_csv('PRSA_Data_Tiantan_20130301-20170228.csv')
    return data

data = load_data()

# Display first few rows of data
st.subheader('Sample Data')
st.write(data.head())

# Summary statistics
st.subheader('Summary Statistics')
st.write(data.describe())

# Visualization - PM2.5 Distribution
st.subheader('PM2.5 Distribution')
fig, ax = plt.subplots()
sns.histplot(data['PM2.5'].dropna(), bins=50, kde=True, ax=ax)
ax.set_title('PM2.5 Distribution')
st.pyplot(fig)

# Visualization - PM10 Distribution
st.subheader('PM10 Distribution')
fig, ax = plt.subplots()
sns.histplot(data['PM10'].dropna(), bins=50, kde=True, ax=ax)
ax.set_title('PM10 Distribution')
st.pyplot(fig)

# Correlation Heatmap
st.subheader('Correlation Matrix')
corr_matrix = data[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'WSPM']].corr()

fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Correlation Matrix of Air Quality Variables')
st.pyplot(fig)

# Time Series Plot - PM2.5, PM10, NO2
st.subheader('Time Series of PM2.5, PM10, and NO2')

# Convert to datetime
data['datetime'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']], errors='coerce')

# Plot time series for PM2.5, PM10, and NO2
fig, ax = plt.subplots(figsize=(14,6))
ax.plot(data['datetime'], data['PM2.5'], label='PM2.5', alpha=0.6)
ax.plot(data['datetime'], data['PM10'], label='PM10', alpha=0.6)
ax.plot(data['datetime'], data['NO2'], label='NO2', alpha=0.6)
ax.legend()
ax.set_title('Time Series of PM2.5, PM10, and NO2')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration')
st.pyplot(fig)

# Conclusion
st.write("""
## Conclusion
The data shows strong correlations between PM2.5, PM10, and NO2. We can also observe seasonal trends in pollutant levels, with significant peaks during certain periods.
""")
