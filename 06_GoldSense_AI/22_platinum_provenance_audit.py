
import pandas as pd
from pathlib import Path

# ============================================================
# 1. FILE PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = (
    BASE_DIR / "data" / "platinum_999_historical.csv"
)

OUTPUT_FILE = (
    BASE_DIR / "data" / "platinum_999_provenance_audit.csv"
)

PRICE_COLUMN = "Platinum_999_PM_Rs_per_10g"

# ============================================================
# 2. LOAD ORIGINAL PLATINUM DATA
# ============================================================

df = pd.read_csv(INPUT_FILE)

df["Date_Parsed"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

# ============================================================
# 3. SOURCE EVIDENCE
# ============================================================

# Secondary-source records:
# India in Data historical platinum rate table.

india_in_data_url = (
    "https://indiaindata.online/platinum-rate-today/"
)

evidence = {

    "14-10-2026": {
        "price": 59147,
        "source": "India in Data - IBJA PM rate",
        "url": india_in_data_url,
        "level": "Secondary source",
        "report_date": ""
    },

    "15-10-2026": {
        "price": 57649,
        "source": "India in Data - IBJA PM rate",
        "url": india_in_data_url,
        "level": "Secondary source",
        "report_date": ""
    },

    "16-10-2026": {
        "price": 58484,
        "source": "India in Data - IBJA PM rate",
        "url": india_in_data_url,
        "level": "Secondary source",
        "report_date": ""
    },

    "19-10-2026": {
        "price": 57026,
        "source": "India in Data - IBJA PM rate",
        "url": india_in_data_url,
        "level": "Secondary source",
        "report_date": ""
    },

    "11-11-2026": {
        "price": 56150,
        "source": "India in Data - IBJA PM rate",
        "url": india_in_data_url,
        "level": "Secondary source",
        "report_date": ""
    },

    "12-11-2026": {
        "price": 54850,
        "source": "India in Data - IBJA PM rate",
        "url": india_in_data_url,
        "level": "Secondary source",
        "report_date": ""
    },

    "13-11-2026": {
        "price": 55940,
        "source": "India in Data - IBJA PM rate",
        "url": india_in_data_url,
        "level": "Secondary source",
        "report_date": ""
    },

    "16-11-2026": {
        "price": 55547,
        "source": "India in Data - IBJA PM rate",
        "url": india_in_data_url,
        "level": "Secondary source",
        "report_date": ""
    },

    # --------------------------------------------------------
    # Primary-source records: IBJA Daily Bullion Reports
    # --------------------------------------------------------

    "06-10-2026": {
        "price": 61285,
        "source": "IBJA Daily Bullion Report",
        "url": (
            "https://ibja.co/Upload/"
            "IBJA_Bullion%20Daily%20Report%20-%2007-10-2026.pdf"
        ),
        "level": "Primary source",
        "report_date": "07-10-2026"
    },

    "07-10-2026": {
        "price": 56095,
        "source": "IBJA Daily Bullion Report",
        "url": (
            "https://ibja.co/Upload/"
            "IBJA_Bullion%20Daily%20Report%20-%2008-10-2026.pdf"
        ),
        "level": "Primary source",
        "report_date": "08-10-2026"
    },

    "28-10-2026": {
        "price": 61706,
        "source": "IBJA Daily Bullion Report",
        "url": (
            "https://ibja.co/Upload/"
            "IBJA_Bullion%20Daily%20Report%20-%2029-10-2026.pdf"
        ),
        "level": "Primary source",
        "report_date": "29-10-2026"
    },

    "05-11-2026": {
        "price": 56863,
        "source": "IBJA Daily Bullion Report",
        "url": (
            "https://ibja.co/Upload/"
            "IBJA_Bullion%20Daily%20Report%20-%2006-11-2026.pdf"
        ),
        "level": "Primary source",
        "report_date": "06-11-2026"
    },

    "06-11-2026": {
        "price": 55707,
        "source": "IBJA Daily Bullion Report",
        "url": (
            "https://www.ibja.co/Upload/"
            "IBJA_Bullion%20Daily%20Report%20-%2009-11-2026.pdf"
        ),
        "level": "Primary source",
        "report_date": "09-11-2026"
    }
}

# ============================================================
# 4. SCRIPT-LISTED PRICE WITHOUT CONFIRMED EVIDENCE
# ============================================================

still_unverified = {

    "07-09-2026": 60837

}

# ============================================================
# 5. CREATE AUDIT COLUMNS
# ============================================================

df["Source"] = ""
df["Source_URL"] = ""
df["Source_Level"] = ""
df["Source_Report_Date"] = ""
df["Verification_Status"] = ""
df["Audit_Notes"] = ""

# ============================================================
# 6. AUDIT COUNTERS
# ============================================================

verified_primary = 0
verified_secondary = 0
unverified_script = 0
unknown_origin = 0
missing_prices = 0
invalid_dates = 0
price_mismatches = 0

# ============================================================
# 7. CHECK EVERY PLATINUM RECORD
# ============================================================

for index, row in df.iterrows():

    date = row["Date_Parsed"]
    price = row[PRICE_COLUMN]

    # --------------------------------------------------------
    # Missing price
    # --------------------------------------------------------

    if pd.isna(price):

        df.at[index, "Verification_Status"] = "Missing"

        df.at[index, "Audit_Notes"] = (
            "No platinum price available."
        )

        missing_prices += 1
        continue

    # --------------------------------------------------------
    # Invalid date
    # --------------------------------------------------------

    if pd.isna(date):

        df.at[index, "Verification_Status"] = (
            "Unverified - invalid date"
        )

        df.at[index, "Audit_Notes"] = (
            "Date could not be parsed."
        )

        invalid_dates += 1
        continue

    date_key = date.strftime("%d-%m-%Y")

    numeric_price = float(price)

    # --------------------------------------------------------
    # Check records with source evidence
    # --------------------------------------------------------

    if date_key in evidence:

        record = evidence[date_key]

        df.at[index, "Source"] = record["source"]

        df.at[index, "Source_URL"] = record["url"]

        df.at[index, "Source_Level"] = record["level"]

        df.at[index, "Source_Report_Date"] = (
            record["report_date"]
        )

        expected_price = record["price"]

        if abs(numeric_price - expected_price) <= 0.01:

            if record["level"] == "Primary source":

                df.at[index, "Verification_Status"] = (
                    "Verified - IBJA report match"
                )

                verified_primary += 1

            else:

                df.at[index, "Verification_Status"] = (
                    "Verified - secondary source match"
                )

                verified_secondary += 1

            df.at[index, "Audit_Notes"] = (
                f"Price matches the recorded source value "
                f"for {date_key}. "
                "Unit: Rs per 10 grams. "
                "Retain the linked evidence for research."
            )

        else:

            df.at[index, "Verification_Status"] = (
                "Unverified - price mismatch"
            )

            df.at[index, "Audit_Notes"] = (
                f"Dataset price: {numeric_price}; "
                f"source price: {expected_price}. "
                "Further investigation required."
            )

            price_mismatches += 1

    # --------------------------------------------------------
    # Script-listed but not independently confirmed
    # --------------------------------------------------------

    elif date_key in still_unverified:

        expected_price = still_unverified[date_key]

        df.at[index, "Source"] = (
            "Claimed source in original script; "
            "independent evidence not located"
        )

        if abs(numeric_price - expected_price) <= 0.01:

            df.at[index, "Verification_Status"] = (
                "Unverified - script-listed"
            )

            df.at[index, "Audit_Notes"] = (
                "Matches the original script entry, "
                "but independent source evidence is still required."
            )

        else:

            df.at[index, "Verification_Status"] = (
                "Unverified - price mismatch"
            )

            df.at[index, "Audit_Notes"] = (
                "Dataset price does not match the original "
                "script entry."
            )

            price_mismatches += 1

        unverified_script += 1

    # --------------------------------------------------------
    # Unknown origin / possible synthetic
    # --------------------------------------------------------

    else:

        df.at[index, "Verification_Status"] = (
            "Unverified - origin unknown (possible synthetic)"
        )

        df.at[index, "Audit_Notes"] = (
            "Not present in the explicitly listed source prices. "
            "Exact origin is unknown. The historical random-fill "
            "block may have populated this record, but this "
            "individual value has not been proven synthetic."
        )

        unknown_origin += 1

# ============================================================
# 8. REMOVE TEMPORARY COLUMN
# ============================================================

df.drop(
    columns=["Date_Parsed"],
    inplace=True
)

# ============================================================
# 9. SAVE SEPARATE AUDIT FILE
# ============================================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ============================================================
# 10. DISPLAY AUDIT REPORT
# ============================================================

print("\nPLATINUM PROVENANCE AUDIT COMPLETED")

print("=" * 60)

print("\nFile information:")

print("Original file preserved:", INPUT_FILE.name)

print("Audit file created:", OUTPUT_FILE.name)

print("\nVerification summary:")

print("Verified - Primary source:", verified_primary)

print("Verified - Secondary source:", verified_secondary)

print("Script-listed but unverified:", unverified_script)

print("Unknown origin / possible synthetic:", unknown_origin)

print("Missing prices:", missing_prices)

print("Invalid dates:", invalid_dates)

print("Price mismatches:", price_mismatches)

print("\nDetailed verification status:")

print(
    df["Verification_Status"]
    .value_counts(dropna=False)
    .to_string()
)

# ============================================================
# 11. DISPLAY VERIFIED RECORDS
# ============================================================

verified_records = df[
    df["Verification_Status"].str.startswith(
        "Verified",
        na=False
    )
]

print("\nVerified records:")

if not verified_records.empty:

    print(
        verified_records[
            [
                "Date",
                PRICE_COLUMN,
                "Source_Level",
                "Verification_Status"
            ]
        ].to_string(index=False)
    )

else:

    print("No verified records found.")

# ============================================================
# 12. FINAL VALIDATION
# ============================================================

print("\nFinal validation:")

print("Total input records:", len(df))

print("Total audit records:", len(df))

print(
    "Original historical CSV modified: No"
)

print(
    "Audit file saved successfully:",
    OUTPUT_FILE.exists()
)

print("\nPLATINUM AUDIT FINISHED")
print("=" * 60)