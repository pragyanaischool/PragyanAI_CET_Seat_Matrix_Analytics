# ui/analytics_page.py

"""
ui/analytics_page.py

Advanced Analytics Page
Smart CET AI Counsellor

Features
--------
✓ District Analytics
✓ Branch Analytics
✓ College Analytics
✓ Year-wise Analytics
✓ HK/RK Analytics
✓ AI/ML Analytics
✓ Seat Growth Analytics
✓ Top Colleges
✓ Top Branches
✓ Heatmaps
✓ Download Reports

Author : PragyanAI
"""

import streamlit as st
import pandas as pd

from ui.charts import (
    district_distribution_chart,
    district_college_count_chart,
    top_districts_chart,

    branch_distribution_chart,
    top_branches_chart,
    course_popularity_chart,

    top_colleges_chart,
    branch_count_per_college,

    growth_chart,
    college_growth_chart,

    hk_analysis_chart,
    rk_analysis_chart,

    aiml_college_chart,
    seat_heatmap
)


# ==========================================================
# PAGE HEADER
# ==========================================================

def analytics_header():

    st.title(
        "📈 Advanced Analytics Dashboard"
    )

    st.markdown(
        """
        Analyze colleges, districts,
        branches, seat growth trends,
        AI/ML expansion and more.
        """
    )


# ==========================================================
# KPI SECTION
# ==========================================================

def render_kpis(df):

    total_colleges = (
        df["college_name"].nunique()
        if "college_name" in df.columns
        else 0
    )

    total_seats = (
        int(df["total_intake"].sum())
        if "total_intake" in df.columns
        else 0
    )

    total_branches = (
        df["course_name"].nunique()
        if "course_name" in df.columns
        else 0
    )

    total_districts = (
        df["district"].nunique()
        if "district" in df.columns
        else 0
    )

    c1, c2, c3, c4 = st.columns(4)

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


# ==========================================================
# DISTRICT TAB
# ==========================================================

def district_tab(df):

    st.subheader(
        "🗺 District Analytics"
    )

    col1, col2 = st.columns(2)

    with col1:
        district_distribution_chart(df)

    with col2:
        district_college_count_chart(df)

    st.divider()

    top_districts_chart(df)


# ==========================================================
# BRANCH TAB
# ==========================================================

def branch_tab(df):

    st.subheader(
        "📚 Branch Analytics"
    )

    col1, col2 = st.columns(2)

    with col1:
        branch_distribution_chart(df)

    with col2:
        course_popularity_chart(df)

    st.divider()

    top_branches_chart(df)


# ==========================================================
# COLLEGE TAB
# ==========================================================

def college_tab(df):

    st.subheader(
        "🏫 College Analytics"
    )

    top_colleges_chart(df)

    st.divider()

    branch_count_per_college(df)

    st.divider()

    if "college_name" in df.columns:

        colleges = sorted(
            df["college_name"]
            .dropna()
            .unique()
        )

        selected_college = st.selectbox(
            "Select College",
            colleges
        )

        if selected_college:

            college_growth_chart(
                df,
                selected_college
            )


# ==========================================================
# YEAR TAB
# ==========================================================

def year_tab(df):

    st.subheader(
        "📈 Year Wise Growth"
    )

    if "year" not in df.columns:

        st.warning(
            "Year data not found."
        )

        return

    growth_chart(df)

    st.divider()

    growth_table = (
        df.groupby("year")
        ["total_intake"]
        .sum()
        .reset_index()
    )

    st.dataframe(
        growth_table,
        use_container_width=True
    )


# ==========================================================
# HK RK TAB
# ==========================================================

def hk_rk_tab(df):

    st.subheader(
        "🌍 HK / RK Analytics"
    )

    col1, col2 = st.columns(2)

    with col1:

        if "hk_seats" in df.columns:
            hk_analysis_chart(df)
        else:
            st.info(
                "HK data unavailable"
            )

    with col2:

        if "rk_seats" in df.columns:
            rk_analysis_chart(df)
        else:
            st.info(
                "RK data unavailable"
            )


# ==========================================================
# AI ML TAB
# ==========================================================

def ai_ml_tab(df):

    st.subheader(
        "🤖 AI / ML Analytics"
    )

    aiml_college_chart(df)

    st.divider()

    ai_df = df[
        df["course_name"]
        .str.contains(
            "ARTIFICIAL",
            case=False,
            na=False
        )
    ]

    st.dataframe(
        ai_df,
        use_container_width=True
    )


# ==========================================================
# HEATMAP TAB
# ==========================================================

def heatmap_tab(df):

    st.subheader(
        "🔥 College vs Branch Heatmap"
    )

    seat_heatmap(df)


# ==========================================================
# INSIGHTS PANEL
# ==========================================================

def analytics_insights(df):

    st.subheader(
        "🧠 AI Generated Insights"
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
            f"""
            Top College:
            {top_college}
            """
        )

        st.success(
            f"""
            Most Popular Branch:
            {top_branch}
            """
        )

        st.success(
            f"""
            Highest Intake District:
            {top_district}
            """
        )

    except:
        pass


# ==========================================================
# DOWNLOAD SECTION
# ==========================================================

def download_section(df):

    st.subheader(
        "📥 Export Analytics"
    )

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="analytics.csv",
        mime="text/csv"
    )


# ==========================================================
# MAIN PAGE
# ==========================================================

def render_analytics(df):

    analytics_header()

    render_kpis(df)

    st.divider()

    analytics_insights(df)

    st.divider()

    (
        tab1,
        tab2,
        tab3,
        tab4,
        tab5,
        tab6,
        tab7
    ) = st.tabs(
        [
            "District",
            "Branch",
            "College",
            "Year",
            "HK/RK",
            "AI/ML",
            "Heatmap"
        ]
    )

    with tab1:
        district_tab(df)

    with tab2:
        branch_tab(df)

    with tab3:
        college_tab(df)

    with tab4:
        year_tab(df)

    with tab5:
        hk_rk_tab(df)

    with tab6:
        ai_ml_tab(df)

    with tab7:
        heatmap_tab(df)

    st.divider()

    download_section(df)


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    st.set_page_config(
        page_title="Analytics",
        layout="wide"
    )

    sample_df = pd.DataFrame({

        "college_name":[
            "BMSCE",
            "RVCE",
            "PES"
        ],

        "district":[
            "Bangalore",
            "Bangalore",
            "Bangalore"
        ],

        "course_name":[
            "CSE",
            "ISE",
            "ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING"
        ],

        "college_type":[
            "Private",
            "Private",
            "Private"
        ],

        "year":[
            2023,
            2024,
            2025
        ],

        "total_intake":[
            1200,
            1500,
            1400
        ],

        "hk_seats":[
            20,
            15,
            10
        ],

        "rk_seats":[
            5,
            8,
            7
        ]
    })

    render_analytics(
        sample_df
    )
```
