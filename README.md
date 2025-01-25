# Chinook - Sales and Performance Dashboard

This project contains a Power BI report with Sales and Performance analysis of an online store named Chinook, designed for study purposes only.

Chinook is a fictitious company, and the dataset has been extracted from the [SQLite Sample Database](https://www.sqlitetutorial.net/sqlite-sample-database/). 

Additionally, this project includes a Python script to extract table data from a SQLite database and export it to CSV format.

<img src=assets\chinook_report.png alt="chinook_report" width="500"/>

**Live version:** [Chinook - Sales and Performance Dashboard](https://app.powerbi.com/view?r=eyJrIjoiOGQ0MjcyZTMtNDE4Ni00N2YxLWFiMDQtYzE2ZDJkN2QwMDQzIiwidCI6IjNmNGRkYWQ2LThiOGItNDRkNS1hOTAyLWI0ODFjZWUwMmFkMyIsImMiOjh9&pageName=ReportSection)


## Table of Contents
- [Key Features](#key-features)
- [Analysis and Insights](#analysis-and-insights)
    - [1. Revenue and Sales performance in 2023](#1-revenue-and-sales-performance-in-2023)
    - [2. Best sellers and most revenue artists in 2023](#2-best-sellers-and-most-revenue-artists-in-2023)
    - [3. Top 3 tracks genre type most sold in 2023](#3-top-3-tracks-genre-type-most-sold-in-2023)
- [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Power BI Report](#1-power-bi-report)
    - [Python Script](#2-python-script)

## Key Features:
- **Power BI Report (.pbip):** Located in `/chinook_report`

- **Dataset (.csv):** Located in `/data`

- **SQLite CSV Extractor (Python script):** Located in `/src`

## Analysis and Insights
### 1. Revenue and sales performance in 2023
- In 2023 (1), sales performance declined compared to the previous year, with all key performance indicators (KPIs) showing a decrease: Revenue (-5.6% vs. PY), Orders (-3.6% vs. PY), and Tracks Sold (-3.6% vs. PY) (2). The most significant drop occurred during the first two quarters (Q1 and Q2).

- A deeper analysis at the Sales Agent level (3) revealed that the agent with the highest margin contribution experienced a sharp decline, with Orders down by -23.8% vs. PY and Revenue down by -33.5% vs. PY.

- From a regional perspective (4), the USA, which historically contributed the most to overall Revenue and Sales, showed a notable decrease in Revenue (-33.5% vs. PY) and Orders (-23.8% vs. PY) this year.
    
    <img src=assets\insight_1.png alt="insight_1" width="500"/>


### 2. Best sellers and most revenue artists in 2023

- In 2023 (1), Iron Maiden was the best-selling artist with 36 tracks sold and generated the highest revenue, totaling $36.6 (2).

    <img src=assets\insight_2.png alt="insight_2" width="500"/>

### 3. Top 3 tracks genre type most sold in 2023

- In 2023 (1), the top 3 genres sold at Chinook were Rock (176 tracks, $174.2 in revenue), Latin (80 tracks, $79.2 in revenue), and Alternative Punk (56 tracks, $55.4 in revenue).

- Targeted sales promotions for these genres could present opportunities to boost both sales and revenue.
    
    <img src=assets\insight_3.png alt="insight_3" width="500"/>


## Installation
### Pre requisites:
- Power BI Desktop
- Python (only required to run the script)

### Power BI Report
- Open the Power BI report (chinook_report/Chinook Dashboard.pbip) in Power BI Desktop.
- Connect the data source by updating the parameter dir_source_data with the directory path where the CSV dataset files are stored on your computer.
- Refresh the data and explore the interactive visuals.
- Customize the visuals to fit your specific requirements.

### Python Script
1. Clone this repository and navigate to its folder.
    ```bash
    git clone https://github.com/lamorasjr/powerbi-chinook-dashboard.git

    cd powerbi-chinook-dashboard.git
    ```

2. Run the Python script to extract data from the SQLite database:
    ```bash
    python src\sqlite_csv_extractor.py
    ```

3. The script will populate the data folder with the dataset tables in csv format. Use it as an input to the Power BI report.
