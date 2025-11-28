import requests
import pandas as pd
import json
import os


def process_covid_data():
# GitHub raw content link (replace USERNAME and REPO)
    GITHUB_USERNAME = "manisha23das"       # your github username
    REPO_NAME = "Covid_19_ETL"

    # API URL to list files in the raw_data/ folder
    API_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/raw_data"

    # 1️⃣ Get list of files in GitHub raw_data folder
    response = requests.get(API_URL)
    files = response.json()

    # Filter only .json files
    json_files = [f for f in files if f["name"].endswith(".json")]

    # Get the latest file based on name (timestamp included)
    latest_file = sorted(json_files, key=lambda x: x["name"], reverse=True)[0]

    # 2️⃣ Download latest JSON file directly (in memory)
    download_url = latest_file["download_url"]
    raw_json = requests.get(download_url).json()

    # 3️⃣ Convert JSON to DataFrame
    df = pd.json_normalize(raw_json)

    # # 4️⃣ Create processed_data folder
    # os.makedirs("processed_data", exist_ok=True)

    # # 5️⃣ Save CSV
    # csv_path = "processed_data/processed_covid_data.csv"

    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_dir = os.path.join(ROOT_DIR, "processed_data")

    os.makedirs(processed_dir, exist_ok=True)

    csv_path = os.path.join(processed_dir, "processed_covid_data.csv")

    df.to_csv(csv_path, index=False)

    return csv_path

    # print(f"Processed CSV saved at: {csv_path}")
    # print(f"Processed the file: {latest_file['name']}")
