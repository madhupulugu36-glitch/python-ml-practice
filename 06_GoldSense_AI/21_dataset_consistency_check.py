
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parent / "data"

FILES = {
    "Gold Historical": "gold_999_historical.csv",
    "Gold Validated": "gold_999_validated.csv",
    "Gold Analysis": "gold_price_analysis.csv",
    "Gold-Platinum Comparison": "gold_platinum_daily_comparison.csv",
    "Platinum Historical": "platinum_999_historical.csv"
}


def load_dataset(filename):

    df = pd.read_csv(DATA / filename)

    raw_dates = df["Date"].astype(str).str.strip()

    iso_mask = raw_dates.str.match(r"^\d{4}-\d{2}-\d{2}$")
    dmy_mask = raw_dates.str.match(r"^\d{2}-\d{2}-\d{4}$")

    parsed_dates = pd.Series(
        pd.NaT,
        index=df.index,
        dtype="datetime64[ns]"
    )

    parsed_dates.loc[iso_mask] = pd.to_datetime(
        raw_dates.loc[iso_mask],
        format="%Y-%m-%d",
        errors="coerce"
    )

    parsed_dates.loc[dmy_mask] = pd.to_datetime(
        raw_dates.loc[dmy_mask],
        format="%d-%m-%Y",
        errors="coerce"
    )

    other_mask = ~(iso_mask | dmy_mask)

    parsed_dates.loc[other_mask] = pd.to_datetime(
        raw_dates.loc[other_mask],
        errors="coerce"
    )

    df["Date"] = parsed_dates

    return df


def compare_prices(base_df, compare_df, column):

    base = base_df[["Date", column]].rename(
        columns={column: "Base_Price"}
    )

    compare = compare_df[["Date", column]].rename(
        columns={column: "Compared_Price"}
    )

    merged = base.merge(
        compare,
        on="Date",
        how="outer",
        indicator=True
    )

    matched = merged[merged["_merge"] == "both"]

    mismatches = matched[
        (matched["Base_Price"] - matched["Compared_Price"]).abs() > 0.01
    ]

    print(f"Matching dates  : {len(matched)}")
    print(f"Missing dates   : {len(merged) - len(matched)}")
    print(f"Price mismatches: {len(mismatches)}")

    if not mismatches.empty:
        print("\nMismatch details:")
        print(mismatches.to_string(index=False))


def main():

    print("\n" + "=" * 75)
    print("       GOLDSENSE AI - DATASET CONSISTENCY CHECK")
    print("=" * 75)

    datasets = {
        name: load_dataset(filename)
        for name, filename in FILES.items()
    }

    gold_sources = [
        "Gold Validated",
        "Gold Analysis",
        "Gold-Platinum Comparison"
    ]

    print("\nGOLD PRICE CONSISTENCY")
    print("-" * 75)

    base = datasets["Gold Historical"]

    for name in gold_sources:

        print(f"\nComparing Gold Historical with {name}")

        compare_prices(
            base,
            datasets[name],
            "Gold_999_PM_Rs_per_10g"
        )

    print("\n" + "-" * 75)
    print("PLATINUM PRICE CONSISTENCY")
    print("-" * 75)

    compare_prices(
        datasets["Platinum Historical"],
        datasets["Gold-Platinum Comparison"],
        "Platinum_999_PM_Rs_per_10g"
    )

    print("\n" + "=" * 75)
    print("CONSISTENCY CHECK COMPLETED")
    print("=" * 75)


if __name__ == "__main__":
    main()