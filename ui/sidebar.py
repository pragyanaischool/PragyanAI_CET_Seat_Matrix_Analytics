"""
ui/sidebar.py

Application Sidebar
"""

import streamlit as st


def render_sidebar(df):
    """
    Main Sidebar

    Returns:
    --------
    {
        "page": str,
        "filtered_df": DataFrame
    }
    """

    st.sidebar.title(
        "🎓 CET Analytics"
    )

    st.sidebar.markdown(
        "---"
    )

    # =====================================
    # NAVIGATION
    # =====================================

    page = st.sidebar.radio(

        "Navigation",

        [

            "Dashboard",

            "Analytics",

            "College Explorer",

            "Comparison",

            "AI Counsellor"
        ]
    )

    filtered_df = df.copy()

    # =====================================
    # FILTERS
    # =====================================

    st.sidebar.markdown(
        "## 🔍 Filters"
    )

    # -------------------------------------
    # YEAR
    # -------------------------------------

    if (
        "year" in filtered_df.columns
        and not filtered_df.empty
    ):

        years = sorted(

            filtered_df["year"]
            .dropna()
            .unique()
            .tolist()
        )

        if years:

            selected_years = (
                st.sidebar.multiselect(

                    "Year",

                    options=years,

                    default=years
                )
            )

            if selected_years:

                filtered_df = filtered_df[

                    filtered_df["year"]
                    .isin(selected_years)
                ]

    # -------------------------------------
    # DISTRICT
    # -------------------------------------

    if (
        "district" in filtered_df.columns
        and not filtered_df.empty
    ):

        districts = sorted(

            filtered_df["district"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        selected_districts = (
            st.sidebar.multiselect(

                "District",

                options=districts
            )
        )

        if selected_districts:

            filtered_df = filtered_df[

                filtered_df["district"]
                .isin(
                    selected_districts
                )
            ]

    # -------------------------------------
    # COLLEGE
    # -------------------------------------

    if (
        "college_name"
        in filtered_df.columns
        and not filtered_df.empty
    ):

        colleges = sorted(

            filtered_df[
                "college_name"
            ]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        selected_colleges = (
            st.sidebar.multiselect(

                "College",

                options=colleges
            )
        )

        if selected_colleges:

            filtered_df = filtered_df[

                filtered_df[
                    "college_name"
                ]
                .isin(
                    selected_colleges
                )
            ]

    # -------------------------------------
    # BRANCH
    # -------------------------------------

    if (
        "course_name"
        in filtered_df.columns
        and not filtered_df.empty
    ):

        branches = sorted(

            filtered_df[
                "course_name"
            ]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        selected_branches = (
            st.sidebar.multiselect(

                "Branch",

                options=branches
            )
        )

        if selected_branches:

            filtered_df = filtered_df[

                filtered_df[
                    "course_name"
                ]
                .isin(
                    selected_branches
                )
            ]

    # =====================================
    # SEARCH
    # =====================================

    st.sidebar.markdown(
        "## 🔎 Quick Search"
    )

    search_text = (
        st.sidebar.text_input(
            "Search College"
        )
    )

    if (
        search_text
        and "college_name"
        in filtered_df.columns
    ):

        filtered_df = filtered_df[

            filtered_df[
                "college_name"
            ]
            .astype(str)
            .str.contains(

                search_text,

                case=False,

                na=False
            )
        ]

    # =====================================
    # DATA SUMMARY
    # =====================================

    st.sidebar.markdown(
        "---"
    )

    st.sidebar.markdown(
        "## 📊 Dataset Summary"
    )

    colleges_count = 0
    seats_count = 0
    branches_count = 0
    districts_count = 0

    if not filtered_df.empty:

        if (
            "college_name"
            in filtered_df.columns
        ):
            colleges_count = (
                filtered_df[
                    "college_name"
                ].nunique()
            )

        if (
            "course_name"
            in filtered_df.columns
        ):
            branches_count = (
                filtered_df[
                    "course_name"
                ].nunique()
            )

        if (
            "district"
            in filtered_df.columns
        ):
            districts_count = (
                filtered_df[
                    "district"
                ].nunique()
            )

        if (
            "total_intake"
            in filtered_df.columns
        ):
            seats_count = int(
                filtered_df[
                    "total_intake"
                ].sum()
            )

    st.sidebar.metric(
        "🏫 Colleges",
        colleges_count
    )

    st.sidebar.metric(
        "🎓 Seats",
        f"{seats_count:,}"
    )

    st.sidebar.metric(
        "📚 Branches",
        branches_count
    )

    st.sidebar.metric(
        "🗺 Districts",
        districts_count
    )

    st.sidebar.markdown(
        "---"
    )

    st.sidebar.caption(
        "PragyanAI CET Seat Matrix Analytics"
    )

    return {

        "page": page,

        "filtered_df":
            filtered_df
    }
    
