# ui/dashboard.py

import streamlit as st
import pandas as pd
from ui.charts import (
    branch_distribution_chart,
    district_distribution_chart,
    college_type_chart
)

def render_dashboard(df):

    st.title("🎓 Smart CET AI Counsellor")

    st.markdown("""
    ### Karnataka CET College Intelligence Platform
    Upload Seat Matrix PDFs and Explore Colleges
    """)

    total_colleges = df["college_name"].nunique()
    total_seats = df["total_intake"].sum()
    total_branches = df["course_name"].nunique()
    total_districts = df["district"].nunique()

    c1,c2,c3,c4 = st.columns(4)

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

    st.divider()

    col1,col2 = st.columns(2)

    with col1:
        branch_distribution_chart(df)

    with col2:
        district_distribution_chart(df)

    st.divider()

    college_type_chart(df)

    st.divider()

    st.subheader("Top Colleges by Intake")

    top = (
        df.groupby("college_name")
        ["total_intake"]
        .sum()
        .sort_values(ascending=False)
        .head(20)
    )

    st.dataframe(
        top.reset_index(),
        use_container_width=True
    )
  
