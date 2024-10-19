<h1>Air Quality Analysis - Tiantan Station</h1>

<p>This repository contains a data analysis project focused on air quality at the <b>Tiantan Station</b>. The analysis is based on a dataset spanning from March 2013 to February 2017. This project is submitted as part of the requirements for the Dicoding program and also serves as a data science portfolio.</p>

<h2>Project Overview</h2>
<p>The goal of this project is to conduct an in-depth analysis of air quality at Tiantan Station, focusing on pollutants such as:</p>
<ul>
    <li><b>PM2.5</b> - Particulate matter with a diameter less than 2.5 micrometers.</li>
    <li><b>PM10</b> - Particulate matter with a diameter less than 10 micrometers.</li>
    <li><b>SO2</b> - Sulfur dioxide.</li>
    <li><b>NO2</b> - Nitrogen dioxide.</li>
    <li><b>CO</b> - Carbon monoxide.</li>
    <li><b>O3</b> - Ozone.</li>
    <li><b>Environmental factors</b> - Temperature, air pressure, wind speed, and precipitation.</li>
</ul>
<p>The dataset was collected over a period of several years at Tiantan Station, and the goal of this analysis is to:</p>
<ul>
    <li>Identify <b>pollution trends</b> over time.</li>
    <li>Investigate <b>correlations between environmental factors</b> (e.g., temperature, wind direction, and wind speed) and pollutant levels.</li>
    <li>Provide insights into potential <b>pollution spikes</b> during specific periods.</li>
</ul>

<h2>Project Structure</h2>
<pre>
air-quality-tiantan-analysis/
│
├── combined_air_quality_data.csv   # Merged dataset used for analysis
├── app.py                          # Streamlit app for interactive visualization
├── analysis.ipynb                  # Jupyter Notebook for detailed data analysis
├── README.md                       # This readme file
├── requirements.txt                # Python libraries required for the project
└── images/                         # Folder for images used in README or Streamlit
</pre>

<h2>Business Questions</h2>
<p>This analysis aims to answer the following business questions:</p>
<ol>
    <li><b>Question 1:</b> What are the trends of PM2.5 levels at Tiantan Station over the period from 2013 to 2017?</li>
    <li><b>Answer:</b> The analysis reveals that there are significant fluctuations in PM2.5 levels, with some seasonal peaks where pollution levels increase, particularly during the winter months.</li>
    
    <li><b>Question 2:</b> Is there a correlation between temperature and PM2.5 levels?</li>
    <li><b>Answer:</b> A correlation analysis shows that as temperatures drop, PM2.5 levels tend to increase. This suggests that colder weather conditions might contribute to higher pollution levels, potentially due to increased heating activities and reduced dispersion of air pollutants.</li>
</ol>

<h2>Analysis Process</h2>
<p>This project follows the full data analysis process, as required by Dicoding:</p>
<ol>
    <li><b>Define Business Questions</b>: The business questions outlined above were defined at the start of the project to guide the analysis.</li>
    <li><b>Data Wrangling</b>: 
        <ul>
            <li>Data was gathered from multiple CSV files and combined into a single dataset for ease of analysis.</li>
            <li>Missing values were handled using the forward fill method, ensuring the completeness of the data.</li>
        </ul>
    </li>
    <li><b>Exploratory Data Analysis (EDA)</b>: 
        <ul>
            <li>Visualizations were created to explore trends in PM2.5 levels over time.</li>
            <li>Correlation analysis was performed to investigate relationships between environmental factors and pollutant levels.</li>
        </ul>
    </li>
    <li><b>Data Visualization</b>: 
        <ul>
            <li>Visualizations were created using Matplotlib and Seaborn to provide insights into air quality trends at Tiantan Station.</li>
            <li>Additionally, Streamlit was used to deploy an interactive dashboard for visualizing the data.</li>
        </ul>
    </li>
    <li><b>Conclusion</b>: 
        <ul>
            <li>The analysis highlights key pollution trends and identifies correlations between weather conditions and pollution levels. Further actions can be taken based on these insights.</li>
        </ul>
    </li>
</ol>

<h2>Technology Used</h2>
<ul>
    <li><b>Python</b>: For data processing using <code>pandas</code>, <code>numpy</code>, and <code>matplotlib</code>.</li>
    <li><b>Jupyter Notebook</b>: For detailed exploratory data analysis (EDA).</li>
    <li><b>Streamlit</b>: For deploying an interactive dashboard in the cloud.</li>
    <li><b>GitHub</b>: For version control and collaboration.</li>
</ul>

<h2>How to Run the Project</h2>
<ol>
    <li><b>Clone the repository</b>:
        <pre><code>git clone https://github.com/WigunaKurniawan/air-quality-tiantan-analysis.git</code></pre>
    </li>
    <li><b>Install dependencies</b>:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><b>Run the Streamlit app</b>:
        <pre><code>streamlit run app.py</code></pre>
    </li>
</ol>

<h2>License</h2>
<p>This project is licensed under the MIT License. You are free to use and modify the code as long as appropriate credit is given.</p>
