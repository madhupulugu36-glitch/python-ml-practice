
import pandas as pd

audit_path = "data/platinum_999_provenance_audit.csv"

df = pd.read_csv(audit_path)

# Dataset rate date: (expected price, official report date, official PDF URL)
verified_records = {
    "12-08-2026": (
        66690, "13-08-2026",
        "https://ibja.co/Upload/IBJA_Bullion%20Daily%20Report%20-%2013-08-2026.pdf"
    ),
    "30-10-2026": (
        53597, "02-11-2026",
        "https://ibja.co/Upload/IBJA_Bullion%20Daily%20Report%20-%2002-11-2026.pdf"
    ),
    "02-11-2026": (
        55453, "03-11-2026",
        "https://ibja.co/Upload/IBJA_Bullion%20Daily%20Report%20-%2003-11-2026.pdf"
    ),
    "03-11-2026": (
        55133, "04-11-2026",
        "https://ibja.co/Upload/IBJA_Bullion%20Daily%20Report%20-%2004-11-2026.pdf"
    ),
    "04-11-2026": (
        53800, "05-11-2026",
        "https://ibja.co/Upload/IBJA_Bullion%20Daily%20Report%20-%2005-11-2026.pdf"
    ),
    "17-11-2026": (
        53107, "18-11-2026",
        "https://ibja.co/Upload/IBJA_Bullion%20Daily%20Report%20-%2018-11-2026.pdf"
    ),
    "18-11-2026": (
        51580, "19-11-2026",
        "https://ibja.co/Upload/IBJA_Bullion%20Daily%20Report%20-%2019-11-2026.pdf"
    ),
    "19-11-2026": (
        51000, "20-11-2026",
        "https://ibja.co/Upload/IBJA_Bullion%20Daily%20Report%20-%2020-11-2026.pdf"
    ),
    "20-11-2026": (
        48730, "23-11-2026",
        "https://ibja.co/Upload/IBJA_Bullion%20Daily%20Report%20-%2023-11-2026.pdf"
    ),
    "23-11-2026": (
        46900, "25-11-2026",
        "https://ibja.co/Upload/IBJA_Bullion%20Daily%20Report%20-%2025-11-2026.pdf"
    )
}

required_columns = [
    "Date",
    "Platinum_999_PM_Rs_per_10g",
    "Source",
    "Source_URL",
    "Source_Level",
    "Source_Report_Date",
    "Verification_Status",
    "Audit_Notes"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing audit columns: {missing_columns}")

df["Date"] = pd.to_datetime(
    df["Date"], dayfirst=True, errors="raise"
).dt.strftime("%d-%m-%Y")

# Validate all records before making any changes.
for date, (expected_price, report_date, url) in verified_records.items():
    matches = df.index[df["Date"] == date].tolist()

    if len(matches) != 1:
        raise ValueError(
            f"Expected exactly one row for {date}; found {len(matches)}"
        )

    current_price = float(
        df.loc[matches[0], "Platinum_999_PM_Rs_per_10g"]
    )

    if abs(current_price - expected_price) > 0.001:
        raise ValueError(
            f"Price mismatch for {date}: "
            f"CSV={current_price}, expected={expected_price}"
        )

# Update only the 10 confirmed records.
for date, (expected_price, report_date, url) in verified_records.items():
    mask = df["Date"] == date

    df.loc[mask, "Source"] = "India Bullion and Jewellers Association (IBJA)"
    df.loc[mask, "Source_URL"] = url
    df.loc[mask, "Source_Level"] = "Primary source - official IBJA report"
    df.loc[mask, "Source_Report_Date"] = report_date
    df.loc[mask, "Verification_Status"] = "Verified - IBJA report match"
    df.loc[mask, "Audit_Notes"] = (
        f"Platinum 999 PM value matches the official IBJA report "
        f"dated {report_date}. Rate applies to {date}. "
        "Original data-entry method remains unknown."
    )

df.to_csv(audit_path, index=False)

print("\nFINAL IBJA PROVENANCE UPDATE COMPLETED")
print("Primary-source records verified:", len(verified_records))
print("Secondary-source records left unchanged: 2")
print("Historical platinum price CSV was not modified.")