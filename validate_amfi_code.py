import pandas as pd
import os
import glob

base_path = r"C:\Users\Padmasri\Desktop\Mutual_Fund_Analytics\data\raw"

fund_file = glob.glob(os.path.join(base_path, "*fund_master*.csv"))[0]
nav_file = glob.glob(os.path.join(base_path, "*nav_history*.csv"))[0]

fund_master = pd.read_csv(fund_file)
nav_history = pd.read_csv(nav_file)

# Get AMFI codes
fund_codes = set(fund_master["amfi_code"].dropna().astype(str))
nav_codes = set(nav_history["amfi_code"].dropna().astype(str))

# Validate
missing_codes = fund_codes - nav_codes
valid_codes = fund_codes & nav_codes

print("===== AMFI CODE VALIDATION =====")
print("Total fund codes:", len(fund_codes))
print("Valid codes:", len(valid_codes))
print("Missing codes:", len(missing_codes))

if missing_codes:
    print("\nMissing AMFI codes:")
    print(missing_codes)
else:
    print("\nAll AMFI codes are validated successfully!")

# Save validation report
report = pd.DataFrame({
    "amfi_code": list(fund_codes),
    "validation_status": [
        "Valid" if code in nav_codes else "Missing"
        for code in fund_codes
    ]
})

report.to_csv(
    os.path.join(base_path, "amfi_validation_report.csv"),
    index=False
)

print("\nValidation report saved successfully!")
