"""
ui/analytics_page.py

Analytics Page
"""

import streamlit as st
import pandas as pd

from analytics.district_analysis import (
    DistrictAnalysis
)

from analytics.branch_analysis import (
    BranchAnalysis
)

from analytics.intake_analysis import (
    IntakeAnalysis
)

from analytics.seat_growth_analysis import (
    SeatGrowthAnalysis
)

from ui.charts import (
    plot_bar_chart,
    plot_line_chart,
    plot_pie_chart
)

def render_analytics(df):
    """
    Analytics Page
    """

    st.title(
        "📊 CET Analytics"
    )

    if df is None or df.empty:

        st.warning(
            "No data available."
        )

        return

    # =====================================
    # ANALYTICS OBJECTS
    # =====================================

    district_analysis = (
        DistrictAnalysis(df)
    )

    branch_analysis = (
        BranchAnalysis(df)
    )

    intake_analysis = (
        IntakeAnalysis(df)
    )

    growth_analysis = (
        SeatGrowthAnalysis(df)
    )

    # =====================================
    # TABS
    # =====================================

    tab1, tab2, tab3, tab4 = st.tabs(

        [

            "District Analysis",

            "Branch Analysis",

            "College Intake",

            "Growth Analysis"
        ]
    )

    # =====================================
    # DISTRICT ANALYSIS
    # =====================================

    with tab1:

        st.subheader(
            "District Wise Seats"
        )

        district_df = (
            district_analysis
            .district_wise_seats()
        )

        st.dataframe(
            district_df,
            use_container_width=True
        )

        if not district_df.empty:

            try:

                fig = plot_bar_chart(

                    district_df,

                    x="district",

                    y="total_intake",

                    title="District Wise Seats"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            except Exception:

                pass

        st.subheader(
            "District Wise Colleges"
        )

        district_colleges = (
            district_analysis
            .district_wise_colleges()
        )

        st.dataframe(
            district_colleges,
            use_container_width=True
        )

    # =====================================
    # BRANCH ANALYSIS
    # =====================================

    with tab2:

        st.subheader(
            "Top Branches"
        )

        branch_df = (
            branch_analysis
            .top_branches()
        )

        st.dataframe(
            branch_df,
            use_container_width=True
        )

        if not branch_df.empty:

            try:

                fig = plot_bar_chart(

                    branch_df.head(15),

                    x="course_name",

                    y="total_intake",

                    title="Top Branches"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            except Exception:

                pass

        st.subheader(
            "Branch College Count"
        )

        college_count_df = (
            branch_analysis
            .branch_college_count()
        )

        st.dataframe(
            college_count_df,
            use_container_width=True
        )

    # =====================================
    # INTAKE ANALYSIS
    # =====================================

    with tab3:

        st.subheader(
            "Top Colleges by Intake"
        )

        intake_df = (
            intake_analysis
            .top_colleges_by_intake()
        )

        st.dataframe(
            intake_df,
            use_container_width=True
        )

        if not intake_df.empty:

            try:

                fig = plot_bar_chart(

                    intake_df.head(20),

                    x="college_name",

                    y="total_intake",

                    title="Top Colleges by Intake"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            except Exception:

                pass

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(

                "Average Intake",

                round(
                    intake_analysis
                    .average_intake(),
                    2
                )
            )

        with col2:

            st.metric(

                "Maximum Intake",

                intake_analysis
                .max_intake()
            )

        with col3:

            st.metric(

                "Minimum Intake",

                intake_analysis
                .min_intake()
            )

    # =====================================
    # GROWTH ANALYSIS
    # =====================================

    with tab4:

        if "year" not in df.columns:

            st.info(
                "Year column not found."
            )

        else:

            st.subheader(
                "Seat Growth Analysis"
            )

            growth_df = (
                growth_analysis
                .overall_growth()
            )

            st.dataframe(
                growth_df,
                use_container_width=True
            )

            if not growth_df.empty:

                try:

                    fig = plot_line_chart(

                        growth_df,

                        x="year",

                        y="total_intake",

                        title="Year Wise Seat Growth"
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

                except Exception:

                    pass

            st.subheader(
                "Highest Growth Colleges"
            )

            growth_colleges = (
                growth_analysis
                .highest_growth_colleges()
            )

            st.dataframe(
                growth_colleges,
                use_container_width=True
            )

    # =====================================
    # RAW DATA
    # =====================================

    with st.expander(
        "View Raw Data"
    ):

        st.dataframe(
            df,
            use_container_width=True
        )
        
