# Chinook - Sales and Performance Dashboard

This project contains a Power BI report with Sales and Performance analysis of an online store named Chinook, designed for study purposes only.

Chinook is a fictitious company, and the dataset has been extracted from the [SQLite Sample Database](https://www.sqlitetutorial.net/sqlite-sample-database/). 

Additionally, this project includes a Python script to extract table data from a SQLite database and export it to CSV format.

### Live version:
- [Chinook - Sales and Performance Dashboard](https://localhost/)


### Key Features:
- **Power BI Report (.pbip):** Located in `/chinook_report`

- **Dataset (.csv):** Located in `/data`

- **SQLite CSV Extractor (Python script):** Located in `/src`

## Table of Contents
- [Analysis and Insights](#analysis-and-insights)
    - [Insight 1](#1-insight-1)
    - [Insight 2](#2-insight-2)
    - [Insight 3](#3-insight-3)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
    - [Power BI Report](#1-power-bi-report)
    - [Python Script](#2-python-script)

## Analysis and Insights
### 1. Insight 1
(Add details about the first insight here.)

### 2. Insight 2
(Add details about the second insight here.)

### 3. Insight 3
(Add details about the third insight here.)

## Prerequisites:
- Power BI Desktop
- Python (only required to run the script)

## Installation
### 1. Power BI Report
- Open the Power BI report (chinook_report/Chinook Dashboard.pbip) in Power BI Desktop.
- Connect the data source by updating the parameter dir_source_data with the directory path where the CSV dataset files are stored on your computer.
- Refresh the data and explore the interactive visuals.
- Customize the visuals to fit your specific requirements.

### 2. Python Script
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