"""
ui/dashboard.py

Main Dashboard
"""

import streamlit as st
import pandas as pd

from ui.charts import (
    district_distribution_chart,
    top_colleges_chart,
    top_branches_chart,
    yearly_growth_chart
)


# =====================================================
# SAFE HELPERS
# =====================================================

def get_colleges_count(df):

    if "college_name" not in df.columns:
        return 0

    return df["college_name"].nunique()


def get_branches_count(df):

    if "course_name" not in df.columns:
        return 0

    return df["course_name"].nunique()


def get_district_count(df):

    if "district" not in df.columns:
        return 0

    return df["district"].nunique()


def get_total_seats(df):

    if "total_intake" not in df.columns:
        return 0

    return int(
        pd.to_numeric(
            df["total_intake"],
            errors="coerce"
        ).fillna(0).sum()
    )


# =====================================================
# KPI SECTION
# =====================================================

def render_kpis(df):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🏫 Colleges",
            get_colleges_count(df)
        )

    with col2:

        st.metric(
            "📚 Branches",
            get_branches_count(df)
        )

    with col3:

        st.metric(
            "🗺 Districts",
            get_district_count(df)
        )

    with col4:

        st.metric(
            "🎓 Total Seats",
            f"{get_total_seats(df):,}"
        )


# =====================================================
# DATA QUALITY
# =====================================================

def render_data_summary(df):

    st.subheader(
        "📋 Dataset Summary"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.write(
            "Rows:",
            len(df)
        )

        st.write(
            "Columns:",
            len(df.columns)
        )

    with c2:

        st.write(
            "Available Fields:"
        )

        st.code(
            ", ".join(
                df.columns.tolist()
            )
        )


# =====================================================
# CHARTS
# =====================================================

def render_charts(df):

    st.subheader(
        "📊 Visual Analytics"
    )

    tab1, tab2, tab3, tab4 = st.tabs(

        [

            "Districts",

            "Branches",

            "Colleges",

            "Growth"
        ]
    )

    # -----------------------------------------

    with tab1:

        if (
            "district" in df.columns
            and
            "total_intake"
            in df.columns
        ):

            fig = (
                district_distribution_chart(
                    df
                )
            )

            if fig:

                st.plotly_chart(

                    fig,

                    use_container_width=True
                )

        else:

            st.info(
                "District data unavailable."
            )

    # -----------------------------------------

    with tab2:

        if (
            "course_name"
            in df.columns
            and
            "total_intake"
            in df.columns
        ):

            fig = (
                top_branches_chart(
                    df
                )
            )

            if fig:

                st.plotly_chart(

                    fig,

                    use_container_width=True
                )

        else:

            st.info(
                "Branch data unavailable."
            )

    # -----------------------------------------

    with tab3:

        if (
            "college_name"
            in df.columns
            and
            "total_intake"
            in df.columns
        ):

            fig = (
                top_colleges_chart(
                    df
                )
            )

            if fig:

                st.plotly_chart(

                    fig,

                    use_container_width=True
                )

        else:

            st.info(
                "College data unavailable."
            )

    # -----------------------------------------

    with tab4:

        if (
            "year"
            in df.columns
            and
            "total_intake"
            in df.columns
        ):

            fig = (
                yearly_growth_chart(
                    df
                )
            )

            if fig:

                st.plotly_chart(

                    fig,

                    use_container_width=True
                )

        else:

            st.info(
                "Year-wise data unavailable."
            )


# =====================================================
# TOP TABLES
# =====================================================

def render_top_tables(df):

    st.subheader(
        "🏆 Top Insights"
    )

    col1, col2 = st.columns(2)

    # -------------------------------------

    with col1:

        if (
            "college_name"
            in df.columns
            and
            "total_intake"
            in df.columns
        ):

            top_colleges = (

                df.groupby(
                    "college_name"
                )["total_intake"]

                .sum()

                .reset_index()

                .sort_values(
                    "total_intake",
                    ascending=False
                )

                .head(10)
            )

            st.write(
                "Top Colleges"
            )

            st.dataframe(
                top_colleges,
                use_container_width=True
            )

    # -------------------------------------

    with col2:

        if (
            "course_name"
            in df.columns
            and
            "total_intake"
            in df.columns
        ):

            top_branches = (

                df.groupby(
                    "course_name"
                )["total_intake"]

                .sum()

                .reset_index()

                .sort_values(
                    "total_intake",
                    ascending=False
                )

                .head(10)
            )

            st.write(
                "Top Branches"
            )

            st.dataframe(
                top_branches,
                use_container_width=True
            )


# =====================================================
# MAIN PAGE
# =====================================================

def render_dashboard(df):

    st.title(
        "🎓 CET Seat Matrix Dashboard"
    )

    if df is None or df.empty:

        st.warning(
            """
            Upload a Seat Matrix
            PDF/CSV/Excel file.
            """
        )

        return

    render_kpis(df)

    st.divider()

    render_data_summary(df)

    st.divider()

    render_charts(df)

    st.divider()

    render_top_tables(df)

    st.divider()

    with st.expander(
        "View Raw Data"
    ):

        st.dataframe(
            df,
            use_container_width=True
        )
        
