import requests
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_FOLDER = BASE_DIR / "data" / "raw"
RAW_FOLDER.mkdir(parents=True, exist_ok=True)

schemes = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

for name, scheme_code in schemes.items():

    print("\nFetching:", name)

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()
        df = pd.DataFrame(data["data"])

        output = RAW_FOLDER / f"{name}_NAV.csv"
        df.to_csv(output, index=False)

        print("Fund:", data["meta"]["scheme_name"])
        print("Records:", len(df))
        print("Saved:", output)

    except Exception as e:
        print("Error:", name, e)

print("\nAll scheme downloads completed!")
