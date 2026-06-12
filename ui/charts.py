"""
ui/charts.py

Reusable Plotly Charts
"""

import plotly.express as px
import plotly.graph_objects as go


# =====================================================
# BAR CHART
# =====================================================

def plot_bar_chart(
    df,
    x,
    y,
    title="",
    color=None
):

    fig = px.bar(
        df,
        x=x,
        y=y,
        color=color,
        title=title
    )

    fig.update_layout(
        height=500
    )

    return fig


# =====================================================
# LINE CHART
# =====================================================

def plot_line_chart(
    df,
    x,
    y,
    title="",
    color=None
):

    fig = px.line(
        df,
        x=x,
        y=y,
        color=color,
        markers=True,
        title=title
    )

    fig.update_layout(
        height=500
    )

    return fig


# =====================================================
# PIE CHART
# =====================================================

def plot_pie_chart(
    df,
    names,
    values,
    title=""
):

    fig = px.pie(
        df,
        names=names,
        values=values,
        title=title
    )

    return fig


# =====================================================
# SCATTER CHART
# =====================================================

def plot_scatter_chart(
    df,
    x,
    y,
    color=None,
    title=""
):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        title=title
    )

    return fig


# =====================================================
# HISTOGRAM
# =====================================================

def plot_histogram(
    df,
    column,
    title=""
):

    fig = px.histogram(
        df,
        x=column,
        title=title
    )

    return fig


# =====================================================
# BOX PLOT
# =====================================================

def plot_box_chart(
    df,
    x,
    y,
    title=""
):

    fig = px.box(
        df,
        x=x,
        y=y,
        title=title
    )

    return fig


# =====================================================
# HEATMAP
# =====================================================

def plot_heatmap(
    pivot_df,
    title="Heatmap"
):

    fig = px.imshow(
        pivot_df,
        text_auto=True,
        aspect="auto",
        title=title
    )

    return fig


# =====================================================
# COLLEGE INTAKE TREND
# =====================================================

def plot_college_growth(
    growth_df,
    title="College Seat Growth"
):

    fig = px.line(
        growth_df,
        x="year",
        y="total_intake",
        markers=True,
        title=title
    )

    return fig


# =====================================================
# DISTRICT SEAT DISTRIBUTION
# =====================================================

def plot_district_distribution(
    district_df
):

    fig = px.bar(
        district_df,
        x="district",
        y="total_intake",
        title="District Wise Seat Distribution"
    )

    return fig


# =====================================================
# BRANCH DISTRIBUTION
# =====================================================

def plot_branch_distribution(
    branch_df
):

    fig = px.bar(
        branch_df,
        x="course_name",
        y="total_intake",
        title="Branch Wise Seats"
    )

    return fig


# =====================================================
# COMPARISON CHART
# =====================================================

def plot_comparison_chart(
    df,
    x,
    y,
    title=""
):

    fig = px.bar(
        df,
        x=x,
        y=y,
        title=title,
        barmode="group"
    )

    return fig


# =====================================================
# KPI TREND CHART
# =====================================================

def plot_kpi_trend(
    values,
    labels,
    title=""
):

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=labels,

            y=values,

            mode="lines+markers"
        )
    )

    fig.update_layout(
        title=title
    )

    return fig
    
# =====================================================
# DISTRICT DISTRIBUTION
# =====================================================

def district_distribution_chart(df):

    if df.empty:
        return None

    district_df = (
        df.groupby("district")["total_intake"]
        .sum()
        .reset_index()
        .sort_values(
            "total_intake",
            ascending=False
        )
    )

    return px.bar(
        district_df,
        x="district",
        y="total_intake",
        title="District Wise Seat Distribution"
    )


# =====================================================
# COLLEGE TYPE
# =====================================================

def college_type_chart(df):

    if (
        df.empty or
        "college_type" not in df.columns
    ):
        return None

    college_type_df = (
        df.groupby("college_type")
        .size()
        .reset_index(name="count")
    )

    return px.pie(
        college_type_df,
        names="college_type",
        values="count",
        title="College Type Distribution"
    )


# =====================================================
# TOP COLLEGES
# =====================================================

def top_colleges_chart(
    df,
    top_n=10
):

    if df.empty:
        return None

    college_df = (
        df.groupby("college_name")
        ["total_intake"]
        .sum()
        .reset_index()
        .sort_values(
            "total_intake",
            ascending=False
        )
        .head(top_n)
    )

    return px.bar(
        college_df,
        x="college_name",
        y="total_intake",
        title=f"Top {top_n} Colleges by Intake"
    )


# =====================================================
# BRANCH DISTRIBUTION
# =====================================================

def branch_distribution_chart(df):

    if df.empty:
        return None

    branch_df = (
        df.groupby("course_name")
        ["total_intake"]
        .sum()
        .reset_index()
        .sort_values(
            "total_intake",
            ascending=False
        )
        .head(20)
    )

    return px.bar(
        branch_df,
        x="course_name",
        y="total_intake",
        title="Branch Distribution"
    )


# =====================================================
# YEAR WISE GROWTH
# =====================================================

def yearly_growth_chart(df):

    if (
        df.empty or
        "year" not in df.columns
    ):
        return None

    growth_df = (
        df.groupby("year")
        ["total_intake"]
        .sum()
        .reset_index()
    )

    return px.line(
        growth_df,
        x="year",
        y="total_intake",
        markers=True,
        title="Year Wise Seat Growth"
    )
    
