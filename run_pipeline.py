import os
import time

# Import functions from other stages
from data_collection.collect_data import collect_covid_data
from data_storage.upload_to_github import upload_raw_files
from data_processing.process_data import process_covid_data
from database_loader import load_to_sqlite

# -----------------------------
# PIPELINE FUNCTION
# -----------------------------
def run_pipeline():

    print("\n🔹 STEP 1: Collecting latest COVID data...")
    raw_file_path = collect_covid_data()
    print(f"✔ Raw data collected: {raw_file_path}")

    print("\n🔹 STEP 2: Uploading raw JSON to GitHub...")
    upload_raw_files()
    print("✔ Raw data synced to GitHub")

    print("\n🔹 STEP 3: Processing latest JSON from GitHub...")
    processed_csv = process_covid_data()
    print(f"✔ Processed CSV created: {processed_csv}")

    print("\n🔹 STEP 4: Loading processed csv data into sqlite")
    load_to_sqlite(processed_csv)
    # print(f"✔ Processed CSV created: {csv_load_to_sqlite}")


    
    print("\n📌 Pipeline completed successfully!\n")


  
# MAIN RUN
# -----------------------------
if __name__ == "__main__":
    run_pipeline()
