
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "data" / "delivery_data_cleaned.csv"
OUTPUT_PATH = BASE_DIR / "data" / "delivery_data_modeling.csv"

df = pd.read_csv(INPUT_PATH)

print("=" * 60)
print("SWIGGY ETA - FEATURE NORMALIZATION")
print("=" * 60)

# 1. Normalize order times
def normalize_order_time(value):
    if pd.isna(value):
        return pd.NA

    value = str(value).strip()

    # Keep valid HH:MM times unchanged
    try:
        parsed = pd.to_datetime(value, format="%H:%M", errors="raise")
        return parsed.strftime("%H:%M")
    except (ValueError, TypeError):
        pass

    # Convert numeric fractions of a day into HH:MM
    try:
        fraction = float(value)
    except ValueError:
        return pd.NA

    # A time fraction must be between 0 (inclusive) and 1 (exclusive)
    if not 0 <= fraction <= 1:
        return pd.NA

    total_minutes = round(fraction * 24 * 60) % (24 * 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60

    return f"{hours:02d}:{minutes:02d}"


original_times = df["Time_Orderd"].copy()
df["Time_Orderd"] = df["Time_Orderd"].apply(normalize_order_time)

converted_count = int(
    (original_times.notna() & df["Time_Orderd"].notna()
     & (original_times.astype("string") != df["Time_Orderd"].astype("string")))
    .sum()
)

print("\n1. ORDER-TIME NORMALIZATION")
print("Original non-missing times:", int(original_times.notna().sum()))
print("Values converted or standardized:", converted_count)
print("Missing times after normalization:", int(df["Time_Orderd"].isna().sum()))
print("\nSample normalized times:")
print(df["Time_Orderd"].value_counts().head(10).to_string())

# 2. Treat ratings above 5 as missing
invalid_rating_mask = (
    df["Delivery_person_Ratings"].notna()
    & ~df["Delivery_person_Ratings"].between(1, 5)
)

invalid_rating_count = int(invalid_rating_mask.sum())
df.loc[invalid_rating_mask, "Delivery_person_Ratings"] = float("nan")

print("\n2. RATING VALIDATION")
print("Ratings outside 1–5:", invalid_rating_count)
print("Missing ratings after validation:",
      int(df["Delivery_person_Ratings"].isna().sum()))

# 3. Save a separate modeling dataset
df.to_csv(OUTPUT_PATH, index=False)

print("\n3. OUTPUT")
print("Dataset shape:", df.shape)
print("Saved to:", OUTPUT_PATH)
print("\nFeature normalization completed.")