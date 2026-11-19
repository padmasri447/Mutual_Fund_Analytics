import pandas as pd
from pathlib import Path

# Project folder location
BASE_DIR = Path(__file__).resolve().parent

# CSV dataset folder
RAW_FOLDER = BASE_DIR / "data" / "raw"

print("Starting Data Ingestion...")

if not RAW_FOLDER.exists():
    print("Error: Raw data folder not found!")

else:
    files = list(RAW_FOLDER.glob("*.csv"))

    print("Total CSV files found:", len(files))

    for file in files:
        print("\n------------------------------")
        print("File Name:", file.name)

        try:
            df = pd.read_csv(file)

            print("Shape:", df.shape)
            print("Columns:", list(df.columns))

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            print("\nMissing Values:")
            print(df.isnull().sum())

            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

        except Exception as e:
            print("Error:", e)

    print("\nData Ingestion Completed!")
