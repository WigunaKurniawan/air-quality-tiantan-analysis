
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title and Introduction
st.title('Proyek Analisis Data: Air Quality Dataset')
st.markdown('''
**Nama**: Wiguna Kurniawan  
**Email**: wiguna_kurniawan@ymail.com  
**ID Dicoding**: Wiguna Kurniawan

---

## Menentukan Pertanyaan Bisnis
1. **Apa tren level PM2.5 di Stasiun Tiantan dari tahun 2013 hingga 2017?**
2. **Apakah ada korelasi antara suhu dan level PM2.5?**
''')

# Load the dataset
data_url = 'https://raw.githubusercontent.com/WigunaKurniawan/air-quality-tiantan-analysis/main/Dataset/PRSA_Data_Tiantan_20130301-20170228.csv'
data = pd.read_csv(data_url)

# Data Cleaning
data_cleaned = data.fillna(method='ffill')
data_cleaned['datetime'] = pd.to_datetime(data_cleaned[['year', 'month', 'day', 'hour']])
data_cleaned.set_index('datetime', inplace=True)

# Show Data Preview
st.subheader('Dataset Preview')
st.write(data_cleaned.head())

# PM2.5 Levels Over Time
st.markdown('### PM2.5 Levels Over Time')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data_cleaned.index, data_cleaned['PM2.5'], color='blue')
ax.set_title('PM2.5 Levels Over Time at Tiantan Station', fontsize=14)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('PM2.5 Concentration', fontsize=12)
st.pyplot(fig)

# Distribution of PM2.5 Categories
st.markdown('### PM2.5 Levels Categorized')
fig, ax = plt.subplots(figsize=(8, 6))
sns.countplot(x='PM2.5_category', data=data_cleaned, palette='Set2', ax=ax)
ax.set_title('Distribution of PM2.5 Levels by Category', fontsize=14)
ax.set_xlabel('PM2.5 Category', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
st.pyplot(fig)

# Correlation Between Temperature and PM2.5
st.markdown('### Correlation Between Temperature and PM2.5')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='TEMP', y='PM2.5', data=data_cleaned, ax=ax)
ax.set_title('Correlation Between Temperature and PM2.5', fontsize=14)
ax.set_xlabel('Temperature (°C)', fontsize=12)
ax.set_ylabel('PM2.5 Concentration', fontsize=12)
st.pyplot(fig)

# Conclusion
st.markdown('''
---

## Conclusion:
1. **PM2.5 levels show seasonal variation**, with higher levels during colder months.
2. **Negative correlation between temperature and PM2.5**: Lower temperatures are associated with higher PM2.5 levels.

This analysis provides insights into how air quality changes with seasonal factors and temperature.
''')
