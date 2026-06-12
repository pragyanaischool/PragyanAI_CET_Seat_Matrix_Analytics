# ui/charts.py
"""
ui/charts.py

Advanced Analytics Charts
For Smart CET AI Counsellor

Author: PragyanAI
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots


# ==========================================================
# COMMON LAYOUT
# ==========================================================

def plot_chart(fig, height=500):
    """
    Common Plotly Layout
    """

    fig.update_layout(
        height=height,
        template="plotly_white",
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),
        title_x=0.5,
        legend=dict(
            orientation="h",
            y=-0.2
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# BRANCH WISE ANALYTICS
# ==========================================================

def branch_distribution_chart(df):

    data = (
        df.groupby("course_name")["total_intake"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        data,
        x="course_name",
        y="total_intake",
        color="total_intake",
        title="Branch Wise Total Intake"
    )

    plot_chart(fig)


# ==========================================================
# TOP BRANCHES
# ==========================================================

def top_branches_chart(df, top_n=15):

    data = (
        df.groupby("course_name")["total_intake"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    fig = px.bar(
        data,
        y="course_name",
        x="total_intake",
        orientation="h",
        color="total_intake",
        title=f"Top {top_n} Branches"
    )

    plot_chart(fig)


# ==========================================================
# DISTRICT ANALYSIS
# ==========================================================

def district_distribution_chart(df):

    data = (
        df.groupby("district")["total_intake"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        data,
        x="district",
        y="total_intake",
        color="total_intake",
        title="District Wise Seats"
    )

    plot_chart(fig)


# ==========================================================
# TOP DISTRICTS
# ==========================================================

def top_districts_chart(df, top_n=15):

    data = (
        df.groupby("district")["total_intake"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    fig = px.bar(
        data,
        y="district",
        x="total_intake",
        orientation="h",
        color="total_intake",
        title=f"Top {top_n} Districts"
    )

    plot_chart(fig)


# ==========================================================
# COLLEGE TYPE ANALYSIS
# ==========================================================

def college_type_chart(df):

    data = (
        df.groupby("college_type")
        ["college_name"]
        .nunique()
        .reset_index()
    )

    fig = px.pie(
        data,
        names="college_type",
        values="college_name",
        hole=0.45,
        title="Government vs Aided vs Private"
    )

    plot_chart(fig)


# ==========================================================
# TOP COLLEGES
# ==========================================================

def top_colleges_chart(df, top_n=20):

    data = (
        df.groupby("college_name")
        ["total_intake"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    fig = px.bar(
        data,
        y="college_name",
        x="total_intake",
        orientation="h",
        color="total_intake",
        title=f"Top {top_n} Colleges By Intake"
    )

    plot_chart(fig, 700)


# ==========================================================
# BRANCH COUNT PER COLLEGE
# ==========================================================

def branch_count_per_college(df):

    data = (
        df.groupby("college_name")
        ["course_name"]
        .nunique()
        .sort_values(ascending=False)
        .head(25)
        .reset_index()
    )

    fig = px.bar(
        data,
        y="college_name",
        x="course_name",
        orientation="h",
        title="Branch Diversity by College"
    )

    plot_chart(fig, 700)


# ==========================================================
# HK ANALYSIS
# ==========================================================

def hk_analysis_chart(df):

    data = (
        df.groupby("district")
        ["hk_seats"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="district",
        y="hk_seats",
        color="hk_seats",
        title="HK Region Seats Distribution"
    )

    plot_chart(fig)


# ==========================================================
# RK ANALYSIS
# ==========================================================

def rk_analysis_chart(df):

    data = (
        df.groupby("district")
        ["rk_seats"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="district",
        y="rk_seats",
        color="rk_seats",
        title="RK Seats Distribution"
    )

    plot_chart(fig)


# ==========================================================
# YEAR WISE GROWTH
# ==========================================================

def growth_chart(df):

    data = (
        df.groupby("year")
        ["total_intake"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        data,
        x="year",
        y="total_intake",
        markers=True,
        title="Year Wise Seat Growth"
    )

    plot_chart(fig)


# ==========================================================
# COLLEGE GROWTH ANALYSIS
# ==========================================================

def college_growth_chart(df, college_name):

    data = (
        df[df["college_name"] == college_name]
        .groupby("year")
        ["total_intake"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        data,
        x="year",
        y="total_intake",
        markers=True,
        title=f"{college_name} Growth Trend"
    )

    plot_chart(fig)


# ==========================================================
# INTAKE COMPARISON
# ==========================================================

def compare_colleges_chart(df, college1, college2):

    d1 = (
        df[df["college_name"] == college1]
        .groupby("course_name")
        ["total_intake"]
        .sum()
        .reset_index()
    )

    d1["college"] = college1

    d2 = (
        df[df["college_name"] == college2]
        .groupby("course_name")
        ["total_intake"]
        .sum()
        .reset_index()
    )

    d2["college"] = college2

    final_df = pd.concat([d1, d2])

    fig = px.bar(
        final_df,
        x="course_name",
        y="total_intake",
        color="college",
        barmode="group",
        title=f"{college1} vs {college2}"
    )

    plot_chart(fig)


# ==========================================================
# COURSE POPULARITY
# ==========================================================

def course_popularity_chart(df):

    data = (
        df.groupby("course_name")
        ["college_name"]
        .nunique()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        data,
        y="course_name",
        x="college_name",
        orientation="h",
        title="Course Popularity Across Colleges"
    )

    plot_chart(fig, 700)


# ==========================================================
# SEAT MATRIX HEATMAP
# ==========================================================

def seat_heatmap(df):

    heat = pd.pivot_table(
        df,
        values="total_intake",
        index="college_name",
        columns="course_name",
        aggfunc="sum",
        fill_value=0
    )

    fig = px.imshow(
        heat,
        title="College vs Branch Heatmap"
    )

    plot_chart(fig, 900)


# ==========================================================
# DISTRICT VS COLLEGE COUNT
# ==========================================================

def district_college_count_chart(df):

    data = (
        df.groupby("district")
        ["college_name"]
        .nunique()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="district",
        y="college_name",
        color="college_name",
        title="District Wise College Count"
    )

    plot_chart(fig)


# ==========================================================
# AI/ML COLLEGE ANALYSIS
# ==========================================================

def aiml_college_chart(df):

    data = df[
        df["course_name"].str.contains(
            "ARTIFICIAL",
            case=False,
            na=False
        )
    ]

    data = (
        data.groupby("college_name")
        ["total_intake"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        data,
        y="college_name",
        x="total_intake",
        orientation="h",
        title="AI & ML Seat Distribution"
    )

    plot_chart(fig, 700)


# ==========================================================
# DASHBOARD SUMMARY
# ==========================================================

def dashboard_summary_charts(df):

    c1, c2 = st.columns(2)

    with c1:
        district_distribution_chart(df)

    with c2:
        college_type_chart(df)

    st.divider()

    c3, c4 = st.columns(2)

    with c3:
        top_branches_chart(df)

    with c4:
        top_colleges_chart(df, 10)
