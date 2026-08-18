# Week 2 – Data Cleaning with Pandas

## Overview

This lab demonstrates a complete **data cleaning workflow** using Python and Pandas. The goal is to transform a messy dataset into a clean and reliable dataset by identifying common data quality issues, applying appropriate cleaning techniques, and validating the final output.

The complete implementation, explanations, and outputs are available in the accompanying Jupyter Notebook.

## Objectives

* Load and inspect a CSV dataset
* Profile missing values
* Fix incorrect data types
* Handle missing values using suitable strategies
* Detect and remove duplicate records
* Identify outliers using the **Interquartile Range (IQR)** method
* Validate and export the cleaned dataset

## Project Structure

```text
data-cleaning/
├── data/
│   ├── employee_data.csv
│   └── employee_data_cleaned.csv
├── notebooks/
│   └── data_cleaning.ipynb
├── src/
│   └── clean_data.py
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
```

## Dataset Issues Covered

The sample dataset intentionally contains multiple real-world data quality problems:

* Missing values
* Incorrect numeric values stored as text
* Invalid date values
* Duplicate records
* Extreme salary outlier

## Data Cleaning Workflow

1. Load the dataset
2. Inspect its structure and data types
3. Profile missing values
4. Convert incorrect data types
5. Handle missing values using median and mode
6. Detect and remove duplicate records
7. Detect outliers using the IQR method
8. Validate the cleaned dataset
9. Export the cleaned CSV

## Key Concepts Practiced

* `pd.read_csv()`
* `df.info()`
* `df.describe()`
* `df.isnull()`
* `pd.to_numeric()`
* `pd.to_datetime()`
* `fillna()`
* `duplicated()`
* `drop_duplicates()`
* `quantile()`
* Interquartile Range (IQR)
* `to_csv(index=False)`

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* JupyterLab (WSL)

## How to Run

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Launch JupyterLab:

```bash
jupyter-lab
```

Open `notebooks/data_cleaning.ipynb` and run the notebook from top to bottom.

## Learning Outcome

By completing this lab, I practiced a complete data cleaning pipeline—from profiling raw data to handling missing values, fixing data types, removing duplicates, detecting outliers using IQR, and exporting a clean dataset for further analysis.

