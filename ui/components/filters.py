# ui/components/filters.py

import streamlit as st


def district_filter(df):

    districts = sorted(
        df["district"]
        .dropna()
        .unique()
    )

    return st.multiselect(
        "District",
        districts
    )


def branch_filter(df):

    branches = sorted(
        df["course_name"]
        .dropna()
        .unique()
    )

    return st.multiselect(
        "Branch",
        branches
    )


def year_filter(df):

    years = sorted(
        df["year"]
        .dropna()
        .unique()
    )

    return st.multiselect(
        "Year",
        years,
        default=years
    )


def college_type_filter(df):

    types = sorted(
        df["college_type"]
        .dropna()
        .unique()
    )

    return st.multiselect(
        "College Type",
        types
    )
