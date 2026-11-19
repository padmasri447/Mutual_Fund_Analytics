import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_FOLDER = BASE_DIR / "data" / "raw"

# Find fund master file
files = list(RAW_FOLDER.glob("*fund_master*"))

if not files:
    print("Fund master file not found!")
else:
    file = files[0]

    print("File found:", file.name)

    df = pd.read_csv(file)

    print("\nDataset Shape:")
    print(df.shape)

    print("\nAll 41 Columns:")
    print(df.columns.tolist())

    print("\nFirst 10 Records:")
    print(df.head(10))

    print("\nFund Houses:")
    print(df.iloc[:, 0].unique())

    print("\nMissing Values:")
    print(df.isnull().sum())
