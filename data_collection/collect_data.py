import requests
import json
import os
from datetime import datetime


def collect_covid_data():
    country = "India"
    url = f"https://disease.sh/v3/covid-19/countries/{country}"

    response = requests.get(url)
    data = response.json()

    data["fetched_at"] = datetime.now().isoformat()

    folder_path = "data_collection/raw_data"
    os.makedirs(folder_path, exist_ok=True)

    filename = f"{folder_path}/covid_data_{country}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    return filename

    # print(f"Data saved to {filename}")

