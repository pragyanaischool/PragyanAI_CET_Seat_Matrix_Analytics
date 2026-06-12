# ui/sidebar.py

"""
ui/sidebar.py

Professional Sidebar
Smart CET AI Counsellor

Features
--------
✓ Navigation
✓ Year Filter
✓ District Filter
✓ Branch Filter
✓ College Type Filter
✓ Upload Seat Matrix
✓ Agent Status
✓ Statistics Summary

Author : PragyanAI
"""

import streamlit as st
import pandas as pd


# ==========================================================
# SIDEBAR LOGO
# ==========================================================

def render_logo():

    st.sidebar.markdown(
        """
        # 🎓 Smart CET
        ### AI Counsellor

        Karnataka College Intelligence Platform
        """
    )


# ==========================================================
# MAIN NAVIGATION
# ==========================================================

def render_navigation():

    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "📌 Navigation",
        [
            "Dashboard",
            "College Explorer",
            "Analytics",
            "Comparison",
            "AI Counsellor"
        ]
    )

    return page


# ==========================================================
# YEAR FILTER
# ==========================================================

def year_filter(df):

    if "year" not in df.columns:
        return None

    years = sorted(
        df["year"].dropna().unique()
    )

    selected_years = st.sidebar.multiselect(
        "📅 Select Year",
        years,
        default=years
    )

    return selected_years


# ==========================================================
# DISTRICT FILTER
# ==========================================================

def district_filter(df):

    if "district" not in df.columns:
        return []

    districts = sorted(
        df["district"]
        .dropna()
        .unique()
    )

    selected_districts = st.sidebar.multiselect(
        "🗺 District",
        districts,
        default=[]
    )

    return selected_districts


# ==========================================================
# BRANCH FILTER
# ==========================================================

def branch_filter(df):

    if "course_name" not in df.columns:
        return []

    branches = sorted(
        df["course_name"]
        .dropna()
        .unique()
    )

    selected_branches = st.sidebar.multiselect(
        "📚 Branch",
        branches,
        default=[]
    )

    return selected_branches


# ==========================================================
# COLLEGE TYPE FILTER
# ==========================================================

def college_type_filter(df):

    if "college_type" not in df.columns:
        return []

    types = sorted(
        df["college_type"]
        .dropna()
        .unique()
    )

    selected_types = st.sidebar.multiselect(
        "🏫 College Type",
        types,
        default=[]
    )

    return selected_types


# ==========================================================
# COLLEGE SEARCH
# ==========================================================

def college_search(df):

    if "college_name" not in df.columns:
        return ""

    colleges = sorted(
        df["college_name"]
        .dropna()
        .unique()
    )

    college = st.sidebar.selectbox(
        "🔍 Search College",
        [""] + list(colleges)
    )

    return college


# ==========================================================
# PDF UPLOAD
# ==========================================================

def upload_section():

    st.sidebar.markdown("---")

    st.sidebar.subheader(
        "📂 Upload Seat Matrix"
    )

    uploaded_files = st.sidebar.file_uploader(
        "Upload PDF Files",
        type=["pdf"],
        accept_multiple_files=True
    )

    return uploaded_files


# ==========================================================
# AGENT STATUS PANEL
# ==========================================================

def agent_status_panel():

    st.sidebar.markdown("---")

    st.sidebar.subheader(
        "🤖 Agent Status"
    )

    st.sidebar.success(
        "PDF Parser Agent : Active"
    )

    st.sidebar.success(
        "Analytics Agent : Active"
    )

    st.sidebar.success(
        "Chat Agent : Active"
    )

    st.sidebar.success(
        "Recommendation Agent : Active"
    )

    st.sidebar.success(
        "College Search Agent : Active"
    )


# ==========================================================
# QUICK STATS
# ==========================================================

def quick_stats(df):

    st.sidebar.markdown("---")

    st.sidebar.subheader(
        "📊 Quick Stats"
    )

    try:

        total_colleges = (
            df["college_name"]
            .nunique()
        )

        total_seats = (
            df["total_intake"]
            .sum()
        )

        total_branches = (
            df["course_name"]
            .nunique()
        )

        total_districts = (
            df["district"]
            .nunique()
        )

        st.sidebar.metric(
            "🏫 Colleges",
            total_colleges
        )

        st.sidebar.metric(
            "🎓 Seats",
            f"{total_seats:,}"
        )

        st.sidebar.metric(
            "📚 Branches",
            total_branches
        )

        st.sidebar.metric(
            "🗺 Districts",
            total_districts
        )

    except:
        pass


# ==========================================================
# APPLY FILTERS
# ==========================================================

def apply_filters(
        df,
        years=None,
        districts=None,
        branches=None,
        college_types=None
):

    filtered_df = df.copy()

    if years:
        filtered_df = filtered_df[
            filtered_df["year"].isin(years)
        ]

    if districts:
        filtered_df = filtered_df[
            filtered_df["district"].isin(districts)
        ]

    if branches:
        filtered_df = filtered_df[
            filtered_df["course_name"].isin(branches)
        ]

    if college_types:
        filtered_df = filtered_df[
            filtered_df["college_type"]
            .isin(college_types)
        ]

    return filtered_df


# ==========================================================
# COMPLETE SIDEBAR
# ==========================================================

def render_sidebar(df):

    render_logo()

    page = render_navigation()

    st.sidebar.markdown("---")

    selected_years = year_filter(df)

    selected_districts = district_filter(df)

    selected_branches = branch_filter(df)

    selected_types = college_type_filter(df)

    selected_college = college_search(df)

    uploaded_files = upload_section()

    agent_status_panel()

    quick_stats(df)

    filtered_df = apply_filters(
        df,
        selected_years,
        selected_districts,
        selected_branches,
        selected_types
    )

    return {
        "page": page,
        "filtered_df": filtered_df,
        "selected_college": selected_college,
        "uploaded_files": uploaded_files,
        "selected_years": selected_years,
        "selected_districts": selected_districts,
        "selected_branches": selected_branches,
        "selected_types": selected_types
    }


# ==========================================================
# TESTING
# ==========================================================

if __name__ == "__main__":

    st.set_page_config(
        page_title="Smart CET",
        layout="wide"
    )

    sample = pd.DataFrame({
        "college_name": [
            "BMSCE",
            "RVCE",
            "PES"
        ],
        "district": [
            "Bangalore",
            "Bangalore",
            "Bangalore"
        ],
        "course_name": [
            "CSE",
            "ISE",
            "ECE"
        ],
        "college_type": [
            "Private",
            "Private",
            "Private"
        ],
        "year": [
            2024,
            2024,
            2025
        ],
        "total_intake": [
            1200,
            1400,
            1300
        ]
    })

    result = render_sidebar(sample)

    st.write(result)
