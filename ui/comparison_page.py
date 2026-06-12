# ui/comparison_page.py
"""
ui/comparison_page.py

College Comparison Engine
Smart CET AI Counsellor

Features
---------
✓ College vs College Comparison
✓ Seat Comparison
✓ Branch Comparison
✓ Placement Comparison
✓ Accreditation Comparison
✓ Year-wise Growth Comparison
✓ Radar Chart
✓ Intake Chart
✓ AI Recommendation
✓ Download Comparison

Author : PragyanAI
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# SELECT COLLEGES
# ==========================================================

def select_colleges(df):

    colleges = sorted(
        df["college_name"]
        .dropna()
        .unique()
    )

    c1, c2 = st.columns(2)

    with c1:

        college1 = st.selectbox(
            "College 1",
            colleges,
            key="college1"
        )

    with c2:

        remaining = [
            c for c in colleges
            if c != college1
        ]

        college2 = st.selectbox(
            "College 2",
            remaining,
            key="college2"
        )

    return college1, college2


# ==========================================================
# SUMMARY METRICS
# ==========================================================

def summary_metrics(
        df,
        college1,
        college2
):

    df1 = df[
        df["college_name"] == college1
    ]

    df2 = df[
        df["college_name"] == college2
    ]

    intake1 = int(
        df1["total_intake"].sum()
    )

    intake2 = int(
        df2["total_intake"].sum()
    )

    branch1 = (
        df1["course_name"]
        .nunique()
    )

    branch2 = (
        df2["course_name"]
        .nunique()
    )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            f"{college1} Seats",
            intake1
        )

        st.metric(
            f"{college1} Branches",
            branch1
        )

    with c2:

        st.metric(
            f"{college2} Seats",
            intake2
        )

        st.metric(
            f"{college2} Branches",
            branch2
        )


# ==========================================================
# SEAT COMPARISON TABLE
# ==========================================================

def seat_comparison_table(
        df,
        college1,
        college2
):

    st.subheader(
        "🎓 Seat Matrix Comparison"
    )

    df1 = (
        df[
            df["college_name"] == college1
        ][
            ["course_name",
             "total_intake"]
        ]
        .rename(
            columns={
                "total_intake":
                college1
            }
        )
    )

    df2 = (
        df[
            df["college_name"] == college2
        ][
            ["course_name",
             "total_intake"]
        ]
        .rename(
            columns={
                "total_intake":
                college2
            }
        )
    )

    comparison = pd.merge(
        df1,
        df2,
        on="course_name",
        how="outer"
    )

    comparison.fillna(
        0,
        inplace=True
    )

    st.dataframe(
        comparison,
        use_container_width=True
    )

    return comparison


# ==========================================================
# BAR CHART
# ==========================================================

def seat_comparison_chart(
        comparison,
        college1,
        college2
):

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=comparison["course_name"],
            y=comparison[college1],
            name=college1
        )
    )

    fig.add_trace(
        go.Bar(
            x=comparison["course_name"],
            y=comparison[college2],
            name=college2
        )
    )

    fig.update_layout(
        title="Branch-wise Seat Comparison",
        barmode="group",
        height=600
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# BRANCH COVERAGE
# ==========================================================

def branch_coverage(
        df,
        college1,
        college2
):

    st.subheader(
        "📚 Branch Coverage"
    )

    branches1 = set(
        df[
            df["college_name"] == college1
        ]["course_name"]
    )

    branches2 = set(
        df[
            df["college_name"] == college2
        ]["course_name"]
    )

    common = (
        branches1.intersection(
            branches2
        )
    )

    only1 = (
        branches1 - branches2
    )

    only2 = (
        branches2 - branches1
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.success(
            f"Common Branches\n\n{len(common)}"
        )

    with c2:

        st.info(
            f"{college1} Exclusive\n\n{len(only1)}"
        )

    with c3:

        st.info(
            f"{college2} Exclusive\n\n{len(only2)}"
        )

    with st.expander(
        "View Branch Details"
    ):

        st.write(
            "Common Branches"
        )

        st.write(
            sorted(common)
        )

        st.write(
            f"{college1} Only"
        )

        st.write(
            sorted(only1)
        )

        st.write(
            f"{college2} Only"
        )

        st.write(
            sorted(only2)
        )


# ==========================================================
# GROWTH COMPARISON
# ==========================================================

def growth_comparison(
        df,
        college1,
        college2
):

    if "year" not in df.columns:
        return

    st.subheader(
        "📈 Year Wise Growth"
    )

    d1 = (
        df[
            df["college_name"] == college1
        ]
        .groupby("year")
        ["total_intake"]
        .sum()
        .reset_index()
    )

    d2 = (
        df[
            df["college_name"] == college2
        ]
        .groupby("year")
        ["total_intake"]
        .sum()
        .reset_index()
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=d1["year"],
            y=d1["total_intake"],
            mode="lines+markers",
            name=college1
        )
    )

    fig.add_trace(
        go.Scatter(
            x=d2["year"],
            y=d2["total_intake"],
            mode="lines+markers",
            name=college2
        )
    )

    fig.update_layout(
        title="Year Wise Seat Growth",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# RADAR CHART
# ==========================================================

def radar_chart(
        df,
        college1,
        college2
):

    st.subheader(
        "🕸 Radar Comparison"
    )

    d1 = df[
        df["college_name"] == college1
    ]

    d2 = df[
        df["college_name"] == college2
    ]

    metrics = [
        "Total Seats",
        "Branches"
    ]

    values1 = [
        d1["total_intake"].sum(),
        d1["course_name"].nunique()
    ]

    values2 = [
        d2["total_intake"].sum(),
        d2["course_name"].nunique()
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values1,
            theta=metrics,
            fill="toself",
            name=college1
        )
    )

    fig.add_trace(
        go.Scatterpolar(
            r=values2,
            theta=metrics,
            fill="toself",
            name=college2
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True
            )
        ),
        height=600
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# ACCREDITATION
# ==========================================================

def accreditation_comparison(
        profile1,
        profile2
):

    st.subheader(
        "🏅 Accreditation Comparison"
    )

    table = pd.DataFrame({

        "Metric":[
            "NAAC",
            "NBA",
            "NIRF"
        ],

        "College 1":[
            profile1.get(
                "naac_grade",
                "N/A"
            ),
            profile1.get(
                "nba_status",
                "N/A"
            ),
            profile1.get(
                "nirf_rank",
                "N/A"
            )
        ],

        "College 2":[
            profile2.get(
                "naac_grade",
                "N/A"
            ),
            profile2.get(
                "nba_status",
                "N/A"
            ),
            profile2.get(
                "nirf_rank",
                "N/A"
            )
        ]
    })

    st.dataframe(
        table,
        use_container_width=True
    )


# ==========================================================
# PLACEMENT COMPARISON
# ==========================================================

def placement_comparison(
        profile1,
        profile2,
        college1,
        college2
):

    st.subheader(
        "💼 Placement Comparison"
    )

    table = pd.DataFrame({

        "Metric":[
            "Highest Package",
            "Average Package",
            "Placement %"
        ],

        college1:[
            profile1.get(
                "highest_package",
                "N/A"
            ),
            profile1.get(
                "average_package",
                "N/A"
            ),
            profile1.get(
                "placement_rate",
                "N/A"
            )
        ],

        college2:[
            profile2.get(
                "highest_package",
                "N/A"
            ),
            profile2.get(
                "average_package",
                "N/A"
            ),
            profile2.get(
                "placement_rate",
                "N/A"
            )
        ]
    })

    st.dataframe(
        table,
        use_container_width=True
    )


# ==========================================================
# AI RECOMMENDATION
# ==========================================================

def ai_recommendation(
        df,
        college1,
        college2
):

    st.subheader(
        "🤖 AI Recommendation"
    )

    score1 = (
        df[
            df["college_name"] == college1
        ]["total_intake"]
        .sum()
    )

    score2 = (
        df[
            df["college_name"] == college2
        ]["total_intake"]
        .sum()
    )

    if score1 > score2:

        st.success(
            f"Recommended: {college1}"
        )

    elif score2 > score1:

        st.success(
            f"Recommended: {college2}"
        )

    else:

        st.info(
            "Both colleges appear comparable."
        )


# ==========================================================
# DOWNLOAD
# ==========================================================

def download_comparison(
        comparison
):

    csv = comparison.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "📥 Download Comparison",
        csv,
        "college_comparison.csv",
        "text/csv"
    )


# ==========================================================
# MAIN PAGE
# ==========================================================

def render_comparison_page(
        df,
        college_profiles=None
):

    st.title(
        "⚖ College Comparison"
    )

    college1, college2 = (
        select_colleges(df)
    )

    summary_metrics(
        df,
        college1,
        college2
    )

    st.divider()

    comparison = (
        seat_comparison_table(
            df,
            college1,
            college2
        )
    )

    seat_comparison_chart(
        comparison,
        college1,
        college2
    )

    st.divider()

    branch_coverage(
        df,
        college1,
        college2
    )

    st.divider()

    growth_comparison(
        df,
        college1,
        college2
    )

    st.divider()

    radar_chart(
        df,
        college1,
        college2
    )

    if college_profiles:

        profile1 = (
            college_profiles.get(
                college1,
                {}
            )
        )

        profile2 = (
            college_profiles.get(
                college2,
                {}
            )
        )

        st.divider()

        accreditation_comparison(
            profile1,
            profile2
        )

        st.divider()

        placement_comparison(
            profile1,
            profile2,
            college1,
            college2
        )

    st.divider()

    ai_recommendation(
        df,
        college1,
        college2
    )

    st.divider()

    download_comparison(
        comparison
    )


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    sample_df = pd.DataFrame({

        "college_name":[
            "BMSCE","BMSCE",
            "RVCE","RVCE"
        ],

        "course_name":[
            "CSE","ISE",
            "CSE","ECE"
        ],

        "total_intake":[
            300,180,
            360,240
        ],

        "year":[
            2023,2023,
            2024,2024
        ]
    })

    render_comparison_page(
        sample_df
    )
