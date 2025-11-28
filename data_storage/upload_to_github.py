import os
import base64
import requests


# -----------------------------
# USER CONFIGURATION
# -----------------------------
GITHUB_USERNAME = "manisha23das"
REPO_NAME = "Covid_19_etl"
FOLDER_IN_REPO = "raw_data"
TOKEN = os.getenv("GITHUB_TOKEN")  # Must be set in environment


# -----------------------------
# GITHUB API URL
# -----------------------------
API_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/{FOLDER_IN_REPO}"


# -----------------------------
# 1. GET LIST OF FILES ALREADY IN GITHUB
# -----------------------------
def get_existing_files():
    response = requests.get(API_URL, headers={"Authorization": f"token {TOKEN}"})
    
    if response.status_code == 200:
        return [file["name"] for file in response.json()]
    else:
        print("Could not fetch existing files:", response.text)
        return []


# -----------------------------
# 2. UPLOAD A SINGLE FILE
# -----------------------------
def upload_file(file_path, file_name):
    with open(file_path, "rb") as f:
        content = f.read()

    encoded_content = base64.b64encode(content).decode("utf-8")

    data = {
        "message": f"Add {file_name}",
        "content": encoded_content
    }

    upload_url = f"{API_URL}/{file_name}"

    response = requests.put(upload_url, json=data, headers={
        "Authorization": f"token {TOKEN}",
        "Content-Type": "application/json"
    })

    if response.status_code in [200, 201]:
        print(f"Uploaded successfully: {file_name}")
    else:
        print(f"Upload FAILED for {file_name}")
        print(response.status_code, response.text)


# -----------------------------
# 3. FUNCTION PIPELINE WILL CALL
# -----------------------------
def upload_raw_files():
    """
    Uploads all JSON files inside data_collection/raw_data
    Returns count of uploaded files
    """

    local_folder = os.path.join(os.path.dirname(__file__), "../data_collection/raw_data")

    if not os.path.exists(local_folder):
        print("Raw data folder not found!")
        return

    existing_files = get_existing_files()
    new_uploads = 0

    for file_name in os.listdir(local_folder):
        file_path = os.path.join(local_folder, file_name)

        if file_name not in existing_files:
            upload_file(file_path, file_name)
            new_uploads += 1
        else:
            print(f"Skipped (already exists): {file_name}")

    return new_uploads


# -----------------------------
# MANUAL RUN
# -----------------------------
if __name__ == "__main__":
    upload_raw_files()
