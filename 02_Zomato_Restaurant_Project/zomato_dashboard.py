from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

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
    file_path = Path(__file__).resolve().parent / "zomato_cleaned.csv"
    return pd.read_csv(file_path)


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

    delivery_data = filtered_df[
        delivery_col
    ].dropna()

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

rating_df = filtered_df[
    filtered_df["Aggregate rating"] > 0
].copy()

if not rating_df.empty:

    fig = px.histogram(
        rating_df,
        x="Aggregate rating",
        nbins=10,
        title="Distribution of Restaurant Ratings",
        labels={
            "Aggregate rating": "Restaurant Rating",
            "count": "Number of Restaurants"
        }
    )

    fig.update_traces(
        hovertemplate=
        "Rating Range: %{x}<br>" +
        "Number of Restaurants: %{y}" +
        "<extra></extra>"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.info(
        "No rating data available for these filters."
    )


# --------------------------------------------------
# 6. RATING VS. COST ANALYSIS
# --------------------------------------------------
st.subheader("💰 Restaurant Rating vs. Cost")

required_columns = [
    "Restaurant Name",
    "Locality",
    "Average Cost for two",
    "Currency",
    "Aggregate rating"
]

cost_rating_df = filtered_df[
    required_columns
].copy()

cost_rating_df = cost_rating_df.dropna()

cost_rating_df = cost_rating_df[
    (cost_rating_df["Aggregate rating"] > 0)
    & (cost_rating_df["Average Cost for two"] > 0)
]

if not cost_rating_df.empty:

    fig = px.scatter(
        cost_rating_df,
        x="Average Cost for two",
        y="Aggregate rating",
        hover_name="Restaurant Name",
        custom_data=[
            "Locality",
            "Average Cost for two",
            "Currency"
        ],
        title="Restaurant Rating vs. Average Cost",
        labels={
            "Average Cost for two": "Average Cost for Two",
            "Aggregate rating": "Restaurant Rating"
        }
    )

    fig.update_traces(
        hovertemplate=
        "<b>%{hovertext}</b><br>" +
        "Area: %{customdata[0]}<br>" +
        "Average Cost for Two: %{customdata[1]:,.0f} " +
        "%{customdata[2]}<br>" +
        "Rating: %{y}<br>" +
        "<extra></extra>"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.info(
        "No cost and rating data available for these filters."
    )


# --------------------------------------------------
# 7. TOP 10 CUISINES
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
        .reset_index()
    )

    cuisine_counts.columns = [
        "Cuisine",
        "Restaurant Count"
    ]

    fig = px.bar(
        cuisine_counts,
        x="Cuisine",
        y="Restaurant Count",
        title="Top 10 Popular Cuisines",
        hover_data={
            "Cuisine": True,
            "Restaurant Count": True
        },
        labels={
            "Cuisine": "Cuisine Type",
            "Restaurant Count": "Number of Restaurants"
        },
        text="Restaurant Count"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        xaxis_tickangle=-45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.info("No restaurants match these filters.")


# --------------------------------------------------
# 8. ONLINE DELIVERY AVAILABILITY
# --------------------------------------------------
st.subheader("🚚 Online Delivery Availability")

if not filtered_df.empty:

    delivery_counts = (
        filtered_df["Has Online delivery"]
        .value_counts()
        .reset_index()
    )

    delivery_counts.columns = [
        "Delivery Status",
        "Restaurant Count"
    ]

    delivery_counts["Delivery Status"] = (
        delivery_counts["Delivery Status"]
        .map({
            "Yes": "Available",
            "No": "Not Available"
        })
        .fillna(delivery_counts["Delivery Status"])
    )

    fig = px.bar(
        delivery_counts,
        x="Delivery Status",
        y="Restaurant Count",
        title="Online Delivery Availability",
        text="Restaurant Count",
        hover_data={
            "Delivery Status": True,
            "Restaurant Count": True
        },
        labels={
            "Delivery Status": "Online Delivery",
            "Restaurant Count": "Number of Restaurants"
        }
    )

    fig.update_layout(
        template="plotly_white",
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.info("No restaurants match these filters.")


# --------------------------------------------------
# 9. DOWNLOAD FILTERED DATA
# --------------------------------------------------
st.subheader("📥 Download Restaurant Data")

csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Filtered Data as CSV",
    data=csv_data,
    file_name="zomato_filtered_restaurants.csv",
    mime="text/csv"
)


# --------------------------------------------------
# 10. DOWNLOAD ANALYSIS REPORT
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

    delivery_data = (
        filtered_df["Has Online delivery"]
        .dropna()
        .astype(str)
        .str.strip()
        .str.lower()
    )

    if not delivery_data.empty:

        delivery_percentage = (
            delivery_data.eq("yes").sum()
            / len(delivery_data)
        ) * 100

        report_lines.append(
            f"Online Delivery Availability: "
            f"{delivery_percentage:.1f}%"
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
            "Restaurant Name",
            "Unknown"
        )

        rating = row["Aggregate rating"]
        votes = row["Votes"]

        report_lines.append(
            f"{restaurant_name} | "
            f"Rating: {rating} | Votes: {votes}"
        )

else:
    report_lines.append(
        "No restaurants match the selected filters."
    )

report_text = "\n".join(report_lines)

st.download_button(
    label="Download Analysis Report",
    data=report_text,
    file_name="zomato_analysis_report.txt",
    mime="text/plain"
)


# --------------------------------------------------
# 11. TOP 10 RESTAURANTS
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

        # Select Top 10 Restaurants
        top_10 = ranking_df.head(10).copy()

        display_columns = [
            col for col in [
                "Restaurant Name",
                "City",
                "Cuisines",
                "Aggregate rating",
                "Votes",
                "Average Cost for two"
            ]
            if col in top_10.columns
        ]

        # Interactive Plotly Chart
        fig = px.bar(
            top_10,
            x="Aggregate rating",
            y="Restaurant Name",
            orientation="h",
            color="Aggregate rating",
            hover_data={
                "City": True,
                "Cuisines": True,
                "Aggregate rating": True,
                "Votes": True,
                "Average Cost for two": True
            },
            title="Top 10 Restaurants by Rating",
            labels={
                "Aggregate rating": "Restaurant Rating",
                "Restaurant Name": "Restaurant"
            }
        )

        fig.update_layout(
            template="plotly_white",
            height=500,
            yaxis={
                "categoryorder": "total ascending"
            }
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Detailed Restaurant Table
        st.dataframe(
            top_10[display_columns],
            width="stretch",
            hide_index=True
        )

    else:
        st.info(
            "No rated restaurants match your filters."
        )

else:
    st.info(
        "No restaurants match your filters."
    )


# --------------------------------------------------
# 12. RESTAURANT DATA TABLE
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
# 13. FOOTER
# --------------------------------------------------
st.success("Dashboard loaded successfully!")
