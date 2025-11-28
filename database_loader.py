import sqlite3
import pandas as pd
import os

def load_to_sqlite(csv_path, db_path="covid_database.db"):
    """
    Loads processed CSV data into a SQLite database.
    Creates the database & table if it does not exist.
    Overwrites the table each time (fresh data load).
    """

    # Check CSV exists
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    print("🔹 STEP 4: Loading processed data into SQLite database...")

    # Load CSV using pandas
    df = pd.read_csv(csv_path)

    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)

    # Load data — replace table each time
    df.to_sql("covid_data", conn, if_exists="replace", index=False)

    conn.close()

    print(f"✔ Data loaded into SQLite DB: {db_path}")
    print("📌 Table name: covid_data")
