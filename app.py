"""
app.py

Smart CET AI Counsellor

Main Entry Point
"""

import streamlit as st
import pandas as pd

from ui.styles import initialize_theme
from ui.sidebar import render_sidebar

from ui.dashboard import render_dashboard
from ui.analytics_page import render_analytics
from ui.college_explorer import (
    render_college_explorer
)
from ui.comparison_page import (
    render_comparison_page
)
from ui.chatbot_ui import (
    render_chatbot
)

from utils.file_utils import (
    load_dataframe
)

from config.settings import (
    settings
)


# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():

    try:

        return load_dataframe(
            "data/processed/colleges.csv"
        )

    except Exception:

        return pd.DataFrame()


# =====================================================
# MAIN
# =====================================================

def main():

    initialize_theme()

    df = load_data()

    if df.empty:

        st.warning(
            """
            No processed college data found.

            Please upload and process
            seat matrix PDFs.
            """
        )

    sidebar_data = render_sidebar(df)

    page = sidebar_data["page"]

    filtered_df = (
        sidebar_data["filtered_df"]
    )

    # ==========================================
    # ROUTING
    # ==========================================

    if page == "Dashboard":

        render_dashboard(
            filtered_df
        )

    elif page == "Analytics":

        render_analytics(
            filtered_df
        )

    elif page == "College Explorer":

        render_college_explorer(
            filtered_df
        )

    elif page == "Comparison":

        render_comparison_page(
            filtered_df
        )

    elif page == "AI Counsellor":

        render_chatbot(
            filtered_df
        )


# =====================================================
# RUN
# =====================================================

if __name__ == "__main__":

    main()
