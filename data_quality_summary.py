import pandas as pd
import os
import glob

base_path = r"C:\Users\Padmasri\Desktop\Mutual_Fund_Analytics\data\raw"

file = glob.glob(os.path.join(base_path, "*fund_master*.csv"))[0]

df = pd.read_csv(file)

print("===== DATA QUALITY SUMMARY =====")

print("\nTotal Records:", len(df))
print("Total Columns:", len(df.columns))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())

print("\nUnique Fund Houses:", df["fund_house"].nunique())

print("\nAMFI Scheme Codes:", df["amfi_code"].nunique())

# Save report
report_path = os.path.join(base_path, "data_quality_summary.txt")

with open(report_path, "w") as f:
    f.write("DATA QUALITY SUMMARY\n")
    f.write(str(df.describe(include="all")))
    f.write("\n\nMissing Values:\n")
    f.write(str(df.isnull().sum()))
    f.write("\n\nDuplicate Records: ")
    f.write(str(df.duplicated().sum()))

print("\nReport saved successfully!")
