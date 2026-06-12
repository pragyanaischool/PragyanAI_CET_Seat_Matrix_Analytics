# ui/dashboard.py

# ui/dashboard.py


"""
ui/dashboard.py

Executive Dashboard
Smart CET AI Counsellor

Author : PragyanAI
"""

import streamlit as st
import pandas as pd

from ui.charts import (
    district_distribution_chart,
    college_type_chart,
    top_colleges_chart,
    top_branches_chart
)


# ==================================================
# HEADER
# ==================================================

def render_header():

    st.title(
        "🎓 Smart CET AI Counsellor"
    )

    st.markdown(
        """
        Karnataka College Intelligence Platform
        """
    )


# ==================================================
# KPI CARDS
# ==================================================

def render_kpis(df):

    total_colleges = (
        df["college_name"].nunique()
    )

    total_seats = (
        int(df["total_intake"].sum())
    )

    total_branches = (
        df["course_name"].nunique()
    )

    total_districts = (
        df["district"].nunique()
    )

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.metric(
            "🏫 Colleges",
            total_colleges
        )

    with c2:
        st.metric(
            "🎓 Seats",
            f"{total_seats:,}"
        )

    with c3:
        st.metric(
            "📚 Branches",
            total_branches
        )

    with c4:
        st.metric(
            "🗺 Districts",
            total_districts
        )


# ==================================================
# QUICK SEARCH
# ==================================================

def quick_search(df):

    st.subheader(
        "🔍 Quick College Search"
    )

    colleges = sorted(
        df["college_name"]
        .dropna()
        .unique()
    )

    selected = st.selectbox(
        "Search College",
        colleges
    )

    if selected:

        college_df = df[
            df["college_name"] == selected
        ]

        st.dataframe(
            college_df,
            use_container_width=True
        )


# ==================================================
# TOP COLLEGES
# ==================================================

def top_colleges_section(df):

    st.subheader(
        "🏆 Top Colleges"
    )

    top_colleges_chart(df)


# ==================================================
# TOP BRANCHES
# ==================================================

def top_branches_section(df):

    st.subheader(
        "📚 Top Branches"
    )

    top_branches_chart(df)


# ==================================================
# ANALYTICS SECTION
# ==================================================

def analytics_section(df):

    col1,col2 = st.columns(2)

    with col1:

        district_distribution_chart(df)

    with col2:

        college_type_chart(df)


# ==================================================
# AI INSIGHTS
# ==================================================

def ai_insights(df):

    st.subheader(
        "🧠 AI Insights"
    )

    try:

        top_college = (
            df.groupby("college_name")
            ["total_intake"]
            .sum()
            .idxmax()
        )

        top_branch = (
            df.groupby("course_name")
            ["total_intake"]
            .sum()
            .idxmax()
        )

        top_district = (
            df.groupby("district")
            ["total_intake"]
            .sum()
            .idxmax()
        )

        st.success(
            f"🏫 Highest Intake College: {top_college}"
        )

        st.success(
            f"📚 Most Popular Branch: {top_branch}"
        )

        st.success(
            f"🗺 Highest Intake District: {top_district}"
        )

    except:
        st.warning(
            "Not enough data."
        )


# ==================================================
# RECENT UPLOADS
# ==================================================

def recent_uploads():

    st.subheader(
        "📂 Uploaded Seat Matrices"
    )

    if "uploaded_files" in st.session_state:

        for file in st.session_state[
            "uploaded_files"
        ]:

            st.info(file.name)

    else:

        st.info(
            "No files uploaded yet."
        )


# ==================================================
# MAIN DASHBOARD
# ==================================================

def render_dashboard(df):

    render_header()

    render_kpis(df)

    st.divider()

    analytics_section(df)

    st.divider()

    col1,col2 = st.columns(2)

    with col1:
        top_colleges_section(df)

    with col2:
        top_branches_section(df)

    st.divider()

    quick_search(df)

    st.divider()

    ai_insights(df)

    st.divider()

    recent_uploads()


# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":

    sample_df = pd.DataFrame({

        "college_name":[
            "BMSCE",
            "RVCE",
            "PES"
        ],

        "district":[
            "Bangalore",
            "Bangalore",
            "Mysore"
        ],

        "course_name":[
            "CSE",
            "ISE",
            "ECE"
        ],

        "total_intake":[
            1200,
            1500,
            1300
        ]
    })

    render_dashboard(sample_df)

