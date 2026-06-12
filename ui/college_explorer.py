# ui/college_explorer.py

"""
ui/college_explorer.py

College Intelligence Explorer

Features
---------
✓ College Search
✓ College Profile
✓ Seat Matrix
✓ Branch Analysis
✓ Year-wise Intake Trend
✓ AI Generated Summary
✓ Placement Information
✓ Accreditation Information
✓ District Information
✓ Compare College
✓ Download College Report

Author: PragyanAI
"""

import streamlit as st
import pandas as pd
import plotly.express as px


# ==========================================================
# COLLEGE SEARCH
# ==========================================================

def college_selector(df):

    colleges = sorted(
        df["college_name"]
        .dropna()
        .unique()
    )

    selected_college = st.selectbox(
        "🔍 Search College",
        colleges
    )

    return selected_college


# ==========================================================
# BASIC PROFILE
# ==========================================================

def render_college_profile(
        college_name,
        college_info
):

    st.title(
        f"🏫 {college_name}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "District",
            college_info.get(
                "district",
                "N/A"
            )
        )

    with col2:

        st.metric(
            "College Type",
            college_info.get(
                "college_type",
                "N/A"
            )
        )

    with col3:

        st.metric(
            "NAAC Grade",
            college_info.get(
                "naac_grade",
                "N/A"
            )
        )


# ==========================================================
# COLLEGE OVERVIEW
# ==========================================================

def render_college_overview(
        college_info
):

    st.subheader(
        "📖 College Overview"
    )

    summary = college_info.get(
        "summary",
        "Information unavailable."
    )

    st.write(summary)


# ==========================================================
# CONTACT INFORMATION
# ==========================================================

def render_contact_info(
        college_info
):

    st.subheader(
        "📞 Contact Information"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.write(
            f"📍 Address: "
            f"{college_info.get('address','N/A')}"
        )

        st.write(
            f"🌐 Website: "
            f"{college_info.get('website','N/A')}"
        )

    with c2:

        st.write(
            f"☎ Phone: "
            f"{college_info.get('phone','N/A')}"
        )

        st.write(
            f"✉ Email: "
            f"{college_info.get('email','N/A')}"
        )


# ==========================================================
# ACCREDITATION
# ==========================================================

def render_accreditation(
        college_info
):

    st.subheader(
        "🏅 Accreditation"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            f"NAAC: "
            f"{college_info.get('naac_grade','N/A')}"
        )

    with col2:

        st.info(
            f"NBA: "
            f"{college_info.get('nba_status','N/A')}"
        )

    with col3:

        st.info(
            f"NIRF: "
            f"{college_info.get('nirf_rank','N/A')}"
        )


# ==========================================================
# PLACEMENT SECTION
# ==========================================================

def render_placements(
        college_info
):

    st.subheader(
        "💼 Placement Statistics"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Highest Package",
            college_info.get(
                "highest_package",
                "N/A"
            )
        )

    with c2:

        st.metric(
            "Average Package",
            college_info.get(
                "average_package",
                "N/A"
            )
        )

    with c3:

        st.metric(
            "Placement %",
            college_info.get(
                "placement_rate",
                "N/A"
            )
        )

    recruiters = college_info.get(
        "recruiters",
        []
    )

    if recruiters:

        st.write(
            "### Top Recruiters"
        )

        st.write(
            ", ".join(recruiters)
        )


# ==========================================================
# SEAT MATRIX
# ==========================================================

def render_seat_matrix(
        college_df
):

    st.subheader(
        "🎓 Seat Matrix"
    )

    columns_to_show = [
        col
        for col in [
            "course_name",
            "total_intake",
            "kea_seats",
            "hk_seats",
            "rk_seats"
        ]
        if col in college_df.columns
    ]

    st.dataframe(
        college_df[columns_to_show],
        use_container_width=True
    )


# ==========================================================
# BRANCH ANALYSIS
# ==========================================================

def render_branch_analysis(
        college_df
):

    st.subheader(
        "📚 Branch Analysis"
    )

    data = (
        college_df.groupby(
            "course_name"
        )["total_intake"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="course_name",
        y="total_intake",
        title="Branch Wise Intake"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# YEAR WISE TREND
# ==========================================================

def render_year_trend(
        df,
        college_name
):

    if "year" not in df.columns:
        return

    st.subheader(
        "📈 Intake Growth Trend"
    )

    trend = (
        df[
            df["college_name"]
            == college_name
        ]
        .groupby("year")
        ["total_intake"]
        .sum()
        .reset_index()
    )

    if len(trend) > 1:

        fig = px.line(
            trend,
            x="year",
            y="total_intake",
            markers=True,
            title="Year Wise Growth"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ==========================================================
# DISTRICT INFO
# ==========================================================

def render_district_info(
        college_info
):

    st.subheader(
        "🗺 District Information"
    )

    st.info(
        college_info.get(
            "district_info",
            "District information unavailable."
        )
    )


# ==========================================================
# AI SUMMARY
# ==========================================================

def render_ai_summary(
        college_info
):

    st.subheader(
        "🤖 AI Generated Insights"
    )

    st.success(
        college_info.get(
            "ai_summary",
            "AI insights unavailable."
        )
    )


# ==========================================================
# COLLEGE COMPARISON
# ==========================================================

def render_comparison_option(
        df,
        current_college
):

    st.subheader(
        "⚖ Compare College"
    )

    colleges = sorted(
        df["college_name"]
        .unique()
    )

    colleges.remove(
        current_college
    )

    compare_with = st.selectbox(
        "Compare With",
        colleges
    )

    return compare_with


# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

def render_download(
        college_df,
        college_name
):

    st.subheader(
        "📥 Download Report"
    )

    csv = (
        college_df
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        label="Download College Data",
        data=csv,
        file_name=f"{college_name}.csv",
        mime="text/csv"
    )


# ==========================================================
# MAIN PAGE
# ==========================================================

def render_college_explorer(
        df,
        college_profiles=None
):

    st.header(
        "🏫 College Explorer"
    )

    selected_college = (
        college_selector(df)
    )

    college_df = df[
        df["college_name"]
        == selected_college
    ]

    if college_profiles:

        college_info = (
            college_profiles.get(
                selected_college,
                {}
            )
        )

    else:

        college_info = {
            "district":
                college_df[
                    "district"
                ].iloc[0]
                if len(college_df)
                else "N/A",

            "college_type":
                college_df[
                    "college_type"
                ].iloc[0]
                if (
                    len(college_df)
                    and "college_type"
                    in college_df.columns
                )
                else "N/A"
        }

    render_college_profile(
        selected_college,
        college_info
    )

    st.divider()

    render_college_overview(
        college_info
    )

    st.divider()

    render_contact_info(
        college_info
    )

    st.divider()

    render_accreditation(
        college_info
    )

    st.divider()

    render_placements(
        college_info
    )

    st.divider()

    render_seat_matrix(
        college_df
    )

    st.divider()

    render_branch_analysis(
        college_df
    )

    st.divider()

    render_year_trend(
        df,
        selected_college
    )

    st.divider()

    render_district_info(
        college_info
    )

    st.divider()

    render_ai_summary(
        college_info
    )

    st.divider()

    render_comparison_option(
        df,
        selected_college
    )

    st.divider()

    render_download(
        college_df,
        selected_college
    )


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    sample = pd.DataFrame({

        "college_name":[
            "BMSCE",
            "BMSCE",
            "RVCE",
            "RVCE"
        ],

        "course_name":[
            "CSE",
            "ISE",
            "CSE",
            "ECE"
        ],

        "district":[
            "Bangalore",
            "Bangalore",
            "Bangalore",
            "Bangalore"
        ],

        "total_intake":[
            300,
            180,
            360,
            240
        ],

        "year":[
            2023,
            2023,
            2024,
            2024
        ]
    })

    render_college_explorer(sample)
