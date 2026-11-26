
from pathlib import Path
import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent / "data"

audited_files = 0
empty_files = 0
error_files = 0

print("\n" + "=" * 75)
print("             GOLDSENSE AI - DATA QUALITY AUDIT")
print("=" * 75)

if not DATA_FOLDER.exists():
    print(f"\nERROR: Data folder not found: {DATA_FOLDER}")

else:
    for file_path in sorted(DATA_FOLDER.glob("*.csv")):

        print("\n" + "-" * 75)
        print(f"DATASET: {file_path.name}")
        print("-" * 75)

        try:
            file_size = file_path.stat().st_size

            print(f"File size           : {file_size:,} bytes")

            # Check empty files before reading
            if file_size == 0:
                print("STATUS              : EMPTY FILE - Cannot audit")
                empty_files += 1
                continue

            df = pd.read_csv(file_path)
            audited_files += 1

            print(f"Total records       : {len(df)}")
            print(f"Total columns       : {len(df.columns)}")
            print(f"Column names        : {list(df.columns)}")

            # Missing value checks
            print("\nMissing values:")
            missing_values = df.isnull().sum()
            print(missing_values.to_string())

            total_missing = int(missing_values.sum())
            print(f"Total missing cells : {total_missing}")

            # Duplicate row checks
            duplicate_rows = df.duplicated().sum()
            print(f"\nDuplicate rows      : {duplicate_rows}")

            # Date column checks
            date_columns = [
                col for col in df.columns
                if "date" in col.lower()
            ]

            if date_columns:

                for date_col in date_columns:

                    raw_dates = (
                        df[date_col]
                        .astype("string")
                        .str.strip()
                    )

                    raw_dates = raw_dates.replace("", pd.NA)

                    # Parse ISO date format
                    iso_dates = pd.to_datetime(
                        raw_dates,
                        format="%Y-%m-%d",
                        errors="coerce"
                    )

                    # Parse Indian day-month-year format
                    dmy_dates = pd.to_datetime(
                        raw_dates,
                        format="%d-%m-%Y",
                        errors="coerce"
                    )

                    dates = iso_dates.fillna(dmy_dates)

                    # Handle remaining valid date/time formats
                    remaining = dates.isna() & raw_dates.notna()

                    if remaining.any():
                        extra_dates = pd.to_datetime(
                            raw_dates.loc[remaining],
                            format="mixed",
                            dayfirst=True,
                            errors="coerce"
                        )

                        dates.loc[remaining] = extra_dates

                    missing_dates = raw_dates.isna().sum()

                    invalid_dates = (
                        raw_dates.notna() & dates.isna()
                    ).sum()

                    valid_dates = dates.dropna()

                    print(f"\nDate column         : {date_col}")
                    print(f"Missing dates       : {missing_dates}")
                    print(f"Invalid dates       : {invalid_dates}")

                    if not valid_dates.empty:

                        print(
                            f"First date          : "
                            f"{valid_dates.min().date()}"
                        )

                        print(
                            f"Last date           : "
                            f"{valid_dates.max().date()}"
                        )

                        print(
                            f"Unique dates        : "
                            f"{valid_dates.nunique()}"
                        )

                        print(
                            f"Duplicate dates     : "
                            f"{valid_dates.duplicated().sum()}"
                        )

                        print("\nYear-wise record count:")

                        year_counts = (
                            valid_dates.dt.year
                            .value_counts()
                            .sort_index()
                        )

                        print(year_counts.to_string())

                    else:
                        print("No valid dates found.")

            else:
                print("\nNo date column identified.")

            # Numeric data checks
            numeric_columns = [
                col for col in df.select_dtypes(
                    include="number"
                ).columns
                if any(
                    keyword in col.lower()
                    for keyword in [
                        "price",
                        "change",
                        "percent",
                        "rate",
                        "value",
                        "rs_per",
                        "amount"
                    ]
                )
            ]

            if numeric_columns:

                print("\nNumeric data checks:")

                for col in numeric_columns:

                    values = df[col].dropna()

                    zero_count = (values == 0).sum()
                    negative_count = (values < 0).sum()

                    print(
                        f"{col}: "
                        f"Zero={zero_count}, "
                        f"Negative={negative_count}"
                    )

            else:
                print("\nNo relevant numeric columns identified.")

            # Sample records
            print("\nSample records:")
            print(df.head(3).to_string(index=False))

        except Exception as error:
            error_files += 1
            print(f"\nERROR: {error}")

# Final audit summary
print("\n" + "=" * 75)
print("                 DATA AUDIT SUMMARY")
print("=" * 75)

print(f"Successfully audited : {audited_files}")
print(f"Empty files           : {empty_files}")
print(f"Files with errors     : {error_files}")
print(
    f"Total CSV files       : "
    f"{audited_files + empty_files + error_files}"
)

print("\n" + "=" * 75)
print("                 DATA AUDIT COMPLETED")
print("=" * 75)