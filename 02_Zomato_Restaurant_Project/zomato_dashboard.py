
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Zomato Restaurant Dashboard",
    page_icon="🍽️",
    layout="wide"
)

# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("02_Zomato_Restaurant_Project/zomato_cleaned.csv")


df = load_data()

st.title("🍽️ Zomato Restaurant Analysis Dashboard")
st.write(
    "Explore restaurant ratings, votes, costs, cuisines, "
    "and online delivery."
)

# --------------------------------------------------
# 3. SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("Restaurant Filters")

# City filter
cities = ["All"] + sorted(
    df["City"].dropna().unique().tolist()
)

selected_city = st.sidebar.selectbox(
    "Select City",
    cities
)

# Minimum rating filter
min_rating = st.sidebar.slider(
    "Minimum Restaurant Rating",
    min_value=0.0,
    max_value=5.0,
    value=0.0,
    step=0.5
)

# Price filter
cost_column = "Average Cost for two"

df[cost_column] = pd.to_numeric(
    df[cost_column],
    errors="coerce"
)

valid_costs = df[cost_column].dropna()

if not valid_costs.empty:
    min_cost = float(valid_costs.min())
    max_cost = float(valid_costs.max())

    selected_cost = st.sidebar.slider(
        "Average Cost for Two",
        min_value=min_cost,
        max_value=max_cost,
        value=(min_cost, max_cost)
    )
else:
    selected_cost = None
    st.sidebar.warning("Cost data is unavailable.")

# Apply filters
filtered_df = df.copy()

if selected_city != "All":
    filtered_df = filtered_df[
        filtered_df["City"] == selected_city
    ]

filtered_df = filtered_df[
    filtered_df["Aggregate rating"] >= min_rating
]

if selected_cost is not None:
    filtered_df = filtered_df[
        filtered_df[cost_column].between(
            selected_cost[0],
            selected_cost[1]
        )
    ]


# --------------------------------------------------
# RESTAURANT SEARCH
# --------------------------------------------------
st.sidebar.subheader("🔎 Search Restaurant")

if "Restaurant Name" in filtered_df.columns:
    search_name = st.sidebar.text_input(
        "Enter restaurant name",
        placeholder="e.g., Domino's Pizza"
    )

    if search_name.strip():
        filtered_df = filtered_df[
            filtered_df["Restaurant Name"]
            .astype(str)
            .str.contains(
                search_name.strip(),
                case=False,
                na=False
            )
        ]
else:
    st.sidebar.info(
        "Restaurant Name column is not available."
    )


# --------------------------------------------------
# 4. KEY PERFORMANCE INDICATORS
# --------------------------------------------------

# --------------------------------------------------
# 4. KEY PERFORMANCE INDICATORS
# --------------------------------------------------
st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

# Total restaurants
col1.metric(
    "Total Restaurants",
    f"{len(filtered_df):,}"
)

# Average rating
rated_df = filtered_df[
    filtered_df["Aggregate rating"] > 0
]

average_rating = rated_df["Aggregate rating"].mean()

col2.metric(
    "Average Rating",
    f"{average_rating:.2f}"
    if pd.notna(average_rating)
    else "N/A"
)

# Total votes
col3.metric(
    "Total Votes",
    f"{filtered_df['Votes'].sum():,.0f}"
)

# Online delivery percentage
delivery_col = "Has Online delivery"

if delivery_col in filtered_df.columns:
    delivery_data = filtered_df[delivery_col].dropna()
    total_with_delivery_info = len(delivery_data)

    if total_with_delivery_info > 0:
        delivery_yes = (
            delivery_data.astype(str)
            .str.strip()
            .str.lower()
            .eq("yes")
            .sum()
        )

        delivery_percentage = (
            delivery_yes / total_with_delivery_info
        ) * 100

        col4.metric(
            "Online Delivery",
            f"{delivery_percentage:.1f}%"
        )
    else:
        col4.metric("Online Delivery", "N/A")
else:
    col4.metric("Online Delivery", "N/A")

st.divider()

# --------------------------------------------------
# 5. RATING DISTRIBUTION
# --------------------------------------------------
st.subheader("⭐ Restaurant Rating Distribution")

if not rated_df.empty:
    fig, ax = plt.subplots(figsize=(9, 4))

    rated_df["Aggregate rating"].hist(
        bins=20,
        ax=ax
    )

    ax.set_xlabel("Restaurant Rating")
    ax.set_ylabel("Number of Restaurants")
    ax.set_title("Distribution of Restaurant Ratings")

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
else:
    st.info("No rated restaurants match these filters.")


# --------------------------------------------------
# RATING VS. COST ANALYSIS
# --------------------------------------------------
st.subheader("💰 Restaurant Rating vs. Cost")

cost_rating_df = filtered_df[
    ["Average Cost for two", "Aggregate rating"]
].dropna()

cost_rating_df = cost_rating_df[
    (cost_rating_df["Aggregate rating"] > 0)
    & (cost_rating_df["Average Cost for two"] > 0)
]

if not cost_rating_df.empty:
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.scatter(
        cost_rating_df["Average Cost for two"],
        cost_rating_df["Aggregate rating"],
        alpha=0.4
    )

    ax.set_xlabel("Average Cost for Two")
    ax.set_ylabel("Restaurant Rating")
    ax.set_title("Restaurant Rating vs. Average Cost")

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
else:
    st.info("No cost and rating data available for these filters.")


# --------------------------------------------------
# 6. TOP 10 CUISINES
# --------------------------------------------------
st.subheader("🍛 Top 10 Popular Cuisines")

if not filtered_df.empty:
    cuisine_counts = (
        filtered_df["Cuisines"]
        .dropna()
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
        .head(10)
    )

    st.bar_chart(cuisine_counts)
else:
    st.info("No restaurants match these filters.")

# --------------------------------------------------
# 7. ONLINE DELIVERY
# --------------------------------------------------
st.subheader("🛵 Online Delivery Availability")

if "Has Online delivery" in filtered_df.columns:
    delivery_counts = (
        filtered_df["Has Online delivery"]
        .fillna("Unknown")
        .value_counts()
    )

    st.bar_chart(delivery_counts)
else:
    st.info("Online delivery data is unavailable.")


# --------------------------------------------------
# DOWNLOAD FILTERED DATA
# --------------------------------------------------
st.subheader("📥 Download Restaurant Data")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data as CSV",
    data=csv_data,
    file_name="zomato_filtered_restaurants.csv",
    mime="text/csv"
)


# --------------------------------------------------
# DOWNLOAD ANALYSIS REPORT
# --------------------------------------------------
st.subheader("📄 Download Analysis Report")

report_lines = [
    "ZOMATO RESTAURANT ANALYSIS REPORT",
    "=" * 40,
    "",
    f"Selected City: {selected_city}",
    f"Minimum Rating Filter: {min_rating}",
    f"Restaurants Analyzed: {len(filtered_df)}",
    f"Average Rating: {average_rating:.2f}"
    if pd.notna(average_rating)
    else "Average Rating: N/A",
    f"Total Votes: {filtered_df['Votes'].sum():,.0f}",
    ""
]

if "Has Online delivery" in filtered_df.columns:
    delivery_data = filtered_df[
        "Has Online delivery"
    ].dropna().astype(str).str.strip().str.lower()

    if not delivery_data.empty:
        delivery_percentage = (
            delivery_data.eq("yes").sum()
            / len(delivery_data)
        ) * 100

        report_lines.append(
            f"Online Delivery Availability: {delivery_percentage:.1f}%"
        )

report_lines.extend([
    "",
    "TOP 10 RESTAURANTS",
    "-" * 40
])

if not filtered_df.empty:
    report_df = filtered_df[
        filtered_df["Aggregate rating"] > 0
    ].sort_values(
        by=["Aggregate rating", "Votes"],
        ascending=[False, False]
    ).head(10)

    for _, row in report_df.iterrows():
        restaurant_name = row.get(
            "Restaurant Name", "Unknown"
        )
        rating = row["Aggregate rating"]
        votes = row["Votes"]

        report_lines.append(
            f"{restaurant_name} | Rating: {rating} | Votes: {votes}"
        )
else:
    report_lines.append("No restaurants match the selected filters.")

report_text = "\n".join(report_lines)

st.download_button(
    label="Download Analysis Report",
    data=report_text,
    file_name="zomato_analysis_report.txt",
    mime="text/plain"
)


# --------------------------------------------------
# TOP 10 RESTAURANTS
# --------------------------------------------------
st.subheader("🏆 Top 10 Restaurants")

if not filtered_df.empty:
    ranking_df = filtered_df[
        filtered_df["Aggregate rating"] > 0
    ].copy()

    if not ranking_df.empty:
        ranking_df = ranking_df.sort_values(
            by=["Aggregate rating", "Votes"],
            ascending=[False, False]
        )

        display_columns = [
            col for col in [
                "Restaurant Name",
                "City",
                "Cuisines",
                "Aggregate rating",
                "Votes",
                "Average Cost for two"
            ]
            if col in ranking_df.columns
        ]

        st.dataframe(
            ranking_df[display_columns].head(10),
            width="stretch",
            hide_index=True
        )
    else:
        st.info("No rated restaurants match your filters.")
else:
    st.info("No restaurants match your filters.")


# --------------------------------------------------
# 8. RESTAURANT DATA TABLE
# --------------------------------------------------
st.subheader("📋 Restaurant Data")

st.caption(
    f"Showing {len(filtered_df):,} restaurants "
    "after applying filters."
)

with st.expander("View Restaurant Data"):
    st.dataframe(
        filtered_df,
        width="stretch"
    )

# --------------------------------------------------
# 9. FOOTER
# --------------------------------------------------
st.success("Dashboard loaded successfully!")
