import requests
import pandas as pd
from pathlib import Path

# Project folder
BASE_DIR = Path(__file__).resolve().parent

# Create raw data folder path
RAW_FOLDER = BASE_DIR / "data" / "raw"
RAW_FOLDER.mkdir(parents=True, exist_ok=True)

# HDFC Top 100 Direct Fund API
url = "https://api.mfapi.in/mf/125497"

print("Fetching live NAV data...")

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    # Convert NAV data into DataFrame
    df = pd.DataFrame(data["data"])

    print("\nFund Name:", data["meta"]["scheme_name"])
    print("\nFirst 5 NAV Records:")
    print(df.head())

    # Save as CSV
    output_file = RAW_FOLDER / "live_nav.csv"
    df.to_csv(output_file, index=False)

    print("\nNAV data saved successfully!")
    print(output_file)

except Exception as e:
    print("Error:", e)
