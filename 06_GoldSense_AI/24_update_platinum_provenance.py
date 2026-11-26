
import pandas as pd

audit_path = "data/platinum_999_provenance_audit.csv"

df = pd.read_csv(audit_path)

# Rate date: (price, report date, source level, URL)
updates = {
    "12-08-2026": (
        66690, "13-08-2026", "IBJA report - URL validation required",
        ""
    ),
    "17-08-2026": (
        63137, "18-08-2026", "Secondary source - Scribd copy",
        ""
    ),
    "25-08-2026": (
        65836, "26-08-2026", "Secondary source - WPS copy",
        ""
    ),
    "30-10-2026": (
        53597, "02-11-2026", "IBJA report - URL validation required",
        ""
    ),
    "02-11-2026": (
        55453, "03-11-2026", "IBJA report - URL validation required",
        ""
    ),
    "03-11-2026": (
        55133, "04-11-2026", "IBJA report - URL validation required",
        ""
    ),
    "04-11-2026": (
        53800, "05-11-2026", "IBJA report - URL validation required",
        ""
    ),
    "17-11-2026": (
        53107, "18-11-2026", "IBJA report - URL validation required",
        ""
    ),
    "18-11-2026": (
        51580, "19-11-2026", "IBJA report - URL validation required",
        ""
    ),
    "19-11-2026": (
        51000, "20-11-2026", "IBJA report - URL validation required",
        ""
    ),
    "20-11-2026": (
        48730, "23-11-2026", "IBJA report - URL validation required",
        ""
    ),
    "23-11-2026": (
        46900, "25-11-2026", "IBJA report - URL validation required",
        ""
    )
}

df["Date"] = pd.to_datetime(
    df["Date"], dayfirst=True, errors="raise"
).dt.strftime("%d-%m-%Y")

updated = 0

for date, (price, report_date, source_level, url) in updates.items():
    mask = df["Date"] == date

    if not mask.any():
        print("Date not found:", date)
        continue

    current_price = df.loc[
        mask, "Platinum_999_PM_Rs_per_10g"
    ].iloc[0]

    if abs(float(current_price) - price) > 0.001:
        print("PRICE MISMATCH - not updated:", date)
        continue

    if "Secondary source" in source_level:
        status = "Secondary source match - direct IBJA confirmation pending"
    else:
        status = "Pending direct IBJA URL validation"

    df.loc[mask, "Source"] = source_level
    df.loc[mask, "Source_URL"] = url
    df.loc[mask, "Source_Level"] = source_level
    df.loc[mask, "Source_Report_Date"] = report_date
    df.loc[mask, "Verification_Status"] = status
    df.loc[mask, "Audit_Notes"] = (
        "Price matches the reported PM rate for this date. "
        "Original data-entry method remains unknown. "
        "Source URL must be validated before final verification."
    )

    updated += 1

df.to_csv(audit_path, index=False)

print("\nProvenance audit updated.")
print("Records updated:", updated)
print("Historical price CSV was not modified.")