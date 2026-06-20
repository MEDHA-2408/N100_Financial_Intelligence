import streamlit as st
import pandas as pd

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="N100 Financial Intelligence",
    layout="wide"
)

st.title("📊 N100 Financial Intelligence Platform")

# ==========================================================
# LOAD DATA
# ==========================================================

health_scores = pd.read_csv(
    "data/processed/health_scores_v2.csv"
)

# ==========================================================
# SIDEBAR
# ==========================================================

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Company Search",
        "Sector Analytics",
        "Investment Screeners",
        "Peer Comparison"
    ]
)

# ==========================================================
# HOME PAGE
# ==========================================================

if page == "Home":

    st.header("Platform Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Companies",
        health_scores["company_id"].nunique()
    )

    col2.metric(
        "Records",
        len(health_scores)
    )

    col3.metric(
        "Average Health Score",
        round(
            health_scores["health_score_v2"].mean(),
            2
        )
    )

    excellent_count = len(
        health_scores[
            health_scores["health_band"] == "Excellent"
        ]
    )

    col4.metric(
        "Excellent Ratings",
        excellent_count
    )

    st.subheader("Health Score Sample")

    st.dataframe(
        health_scores[
            [
                "company_id",
                "year",
                "health_score_v2",
                "health_band"
            ]
        ].head(20)
    )

# ==========================================================
# COMPANY SEARCH
# ==========================================================

elif page == "Company Search":

    st.header("Company Search")

    company_list = sorted(
        health_scores["company_id"].unique()
    )

    selected_company = st.selectbox(
        "Select Company",
        company_list
    )

    company_data = health_scores[
        health_scores["company_id"]
        == selected_company
    ]

    st.subheader(
        f"{selected_company} Financial Health"
    )

    st.dataframe(company_data)

    st.line_chart(
        company_data.set_index("year")
        ["health_score_v2"]
    )

# ==========================================================
# SECTOR ANALYTICS
# ==========================================================

elif page == "Sector Analytics":

    st.header("Sector Analytics")

    sector_data = pd.read_csv(
        "data/processed/sector_analytics.csv"
    )

    st.subheader("Sector Ranking")

    st.dataframe(sector_data)

    st.subheader(
        "Average Health Score by Sector"
    )

    st.bar_chart(
        sector_data.set_index("sector")
        ["avg_health_score"]
    )

    st.subheader("🏆 Top 10 Companies")

    top_companies = (
        health_scores[
            health_scores["year"] == "Mar 2024"
        ]
        .drop_duplicates(
            subset=["company_id"]
        )
        .sort_values(
            by="health_score_v2",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top_companies[
            [
                "company_id",
                "health_score_v2",
                "health_band"
            ]
        ]
    )

# ==========================================================
# INVESTMENT SCREENERS
# ==========================================================

elif page == "Investment Screeners":

    st.header("Investment Screeners")

    quality_growth = pd.read_csv(
        "data/processed/quality_growth_screener.csv"
    )

    debt_free = pd.read_csv(
        "data/processed/debt_free_screener.csv"
    )

    high_roe = pd.read_csv(
        "data/processed/high_roe_screener.csv"
    )

    turnaround = pd.read_csv(
        "data/processed/turnaround_screener.csv"
    )

    screener = st.selectbox(
        "Choose Screener",
        [
            "Quality Growth",
            "Debt Free",
            "High ROE",
            "Turnaround"
        ]
    )

    if screener == "Quality Growth":
        st.dataframe(quality_growth)

    elif screener == "Debt Free":
        st.dataframe(debt_free)

    elif screener == "High ROE":
        st.dataframe(high_roe)

    elif screener == "Turnaround":
        st.dataframe(turnaround)

# ==========================================================
# PEER COMPARISON
# ==========================================================

elif page == "Peer Comparison":

    st.header("Peer Comparison")

    peer_data = pd.read_csv(
        "data/processed/peer_comparison.csv"
    )

    company_list = sorted(
        peer_data["company_id"].unique()
    )

    selected_company = st.selectbox(
        "Select Company",
        company_list
    )

    company_info = peer_data[
        peer_data["company_id"]
        == selected_company
    ]

    st.subheader(
        f"{selected_company} Peer Analysis"
    )

    st.dataframe(
        company_info[
            [
                "company_id",
                "broad_sector",
                "health_score_v2",
                "sector_avg_score",
                "difference_from_sector"
            ]
        ]
    )