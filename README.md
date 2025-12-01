# COVID-19 Daily ETL Pipeline (Python + GitHub Actions)
A fully automated ETL (Extract–Transform–Load) pipeline built for learning and demonstration purposes.
The pipeline fetches real-time COVID-19 data from a public API, processes it into clean tabular format (CSV), and stores the output inside the repository.
Daily runs are automated using GitHub Actions, showcasing skills in scheduling, data processing, and workflow orchestration.

## Project Overview
### This project demonstrates a complete End-to-End ETL workflow using:
Python
GitHub Actions (Automation)
API Data Extraction
Data Cleaning & Transformation
JSON → CSV Conversion
(Local) SQLite Database Loading

### The pipeline collects fresh COVID-19 data every day and updates the repository with:
A new raw JSON file
An updated processed CSV file

## Tech Stack
Python (requests, pandas)
GitHub Actions (CI/CD automation)
JSON → CSV Processing
SQLite (loading)

## Workflow Explanation
### Automated Daily ETL using GitHub Actions

Scheduled workflow runs every morning (or manually on trigger)
Automatically extracts the latest COVID-19 data
Processes the raw JSON into structured CSV
Commits updated data back into the repository

## Project Structure
covid_19_etl/
│
├── .github/
│   └── workflows/
│       └── run_pipeline.yml          # GitHub Actions workflow (automation)
│
├── data_collection/
│   ├── raw_data/                     # Local folder where collect_data.py saves raw JSON files
│   │   └── covid_data_<timestamp>.json
│   └── collect_data.py               # Script: call API → save raw JSON (returns filename)
│
├── data_processing/
│   └── process_data.py               # Script: read latest JSON from repo/GitHub → convert to CSV
│
├── data_storage/
│   └── upload_to_github.py           # Script: upload raw JSON files (or processed CSV) to GitHub via API
│
├── processed_data/
│   └── processed_covid_data.csv      # Processed CSV produced by process_data.py
│
├── database_loader.py                # Script: load processed CSV into local SQLite DB (covid_database.db)
│
├── run_pipeline.py                   # Orchestrator: calls collect → upload → process → load
│
├── covid_database.db                 # Local SQLite DB
│
├── requirements.txt                  # pip dependencies: requests, pandas, etc.
├── .gitignore
└── README.md

## Key Learnings

Working with real-time APIs
JSON & CSV data handling
Automating pipelines using GitHub Actions
Designing ETL workflows
Structuring real-world data projects

## Future Improvements

Host processed data on cloud storage (S3 / GCS)
Add dashboards (Power BI / Tableau)
Cloud migration pipeline
Automated email notification on ETL failure
