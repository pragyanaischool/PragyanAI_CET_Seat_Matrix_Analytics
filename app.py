"""
app.py

PragyanAI CET Seat Matrix Analytics
Main Streamlit Application
"""

import streamlit as st
import pandas as pd
import tempfile
from pathlib import Path

# ==========================================
# CONFIG
# ==========================================

from config.settings import settings

# ==========================================
# UI
# ==========================================

from ui.styles import initialize_theme

from ui.sidebar import render_sidebar

from ui.dashboard import render_dashboard

from ui.analytics_page import (
    render_analytics
)

from ui.college_explorer import (
    render_college_explorer
)

from ui.comparison_page import (
    render_comparison_page
)

from ui.chatbot_ui import (
    render_chatbot
)

# ==========================================
# EXTRACTION
# ==========================================

from extraction.pdf_parser import (
    PDFParser
)

from extraction.table_extractor import (
    TableExtractor
)

from extraction.seat_matrix_parser import (
    SeatMatrixParser
)

# ==========================================
# RAG
# ==========================================

from rag.vectorstore import (
    vector_store
)

# ==========================================
# UTILS
# ==========================================

from utils.logger import (
    get_logger
)

logger = get_logger(__name__)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(

    page_title=settings.PAGE_TITLE,

    page_icon=settings.PAGE_ICON,

    layout=settings.LAYOUT
)

# ==========================================
# SESSION STATE
# ==========================================

if "seat_matrix_df" not in st.session_state:

    st.session_state["seat_matrix_df"] = (
        pd.DataFrame()
    )

if "data_loaded" not in st.session_state:

    st.session_state["data_loaded"] = False

if "vector_indexed" not in st.session_state:

    st.session_state["vector_indexed"] = False


# ==========================================
# HELPERS
# ==========================================

def load_default_data():

    processed_file = (
        Path(
            "data/processed/colleges.csv"
        )
    )

    if processed_file.exists():

        try:

            df = pd.read_csv(
                processed_file
            )

            st.session_state[
                "seat_matrix_df"
            ] = df

            st.session_state[
                "data_loaded"
            ] = True

            return True

        except Exception as e:

            logger.error(str(e))

    return False


def process_pdf(pdf_file):

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(
                pdf_file.read()
            )

            pdf_path = temp_file.name

        extractor = (
            TableExtractor()
        )

        parser = (
            SeatMatrixParser()
        )

        raw_df = (
            extractor.tables_to_dataframe(
                pdf_path
            )
        )

        df = parser.parse(
            raw_df
        )

        return df

    except Exception as e:

        logger.error(
            f"PDF Error: {str(e)}"
        )

        st.error(
            f"PDF Parsing Failed: {str(e)}"
        )

        return pd.DataFrame()


def process_csv(uploaded_file):

    try:

        return pd.read_csv(
            uploaded_file
        )

    except Exception as e:

        st.error(str(e))

        return pd.DataFrame()


def process_excel(uploaded_file):

    try:

        return pd.read_excel(
            uploaded_file
        )

    except Exception as e:

        st.error(str(e))

        return pd.DataFrame()


def index_dataframe(df):

    if df.empty:

        return

    try:

        documents = []

        for _, row in df.iterrows():

            doc = f"""

            College Name:
            {row.get('college_name','')}

            District:
            {row.get('district','')}

            Branch:
            {row.get('course_name','')}

            Intake:
            {row.get('total_intake',0)}

            Year:
            {row.get('year','')}

            """

            documents.append(doc)

        if documents:

            vector_store.add_documents(
                documents
            )

            st.session_state[
                "vector_indexed"
            ] = True

    except Exception as e:

        logger.error(
            f"Vector Index Error: {str(e)}"
        )


# ==========================================
# LOAD DEFAULT DATA
# ==========================================

if not st.session_state["data_loaded"]:

    load_default_data()


# ==========================================
# UI THEME
# ==========================================

initialize_theme()

# ==========================================
# TITLE
# ==========================================

st.title(
    "🎓 PragyanAI CET Seat Matrix Analytics"
)

st.caption(
    """
    Upload KCET Seat Matrix PDFs,
    Analyze Colleges,
    Compare Trends,
    Explore District Analytics,
    AI Counsellor
    """
)

# ==========================================
# FILE UPLOAD
# ==========================================

uploaded_file = st.file_uploader(

    "Upload Seat Matrix File",

    type=[
        "pdf",
        "csv",
        "xlsx"
    ]
)

if uploaded_file:

    file_type = (
        uploaded_file.name
        .split(".")[-1]
        .lower()
    )

    with st.spinner(
        "Processing file..."
    ):

        if file_type == "pdf":

            df = process_pdf(
                uploaded_file
            )

        elif file_type == "csv":

            df = process_csv(
                uploaded_file
            )

        elif file_type == "xlsx":

            df = process_excel(
                uploaded_file
            )

        else:

            df = pd.DataFrame()

        if not df.empty:

            st.session_state[
                "seat_matrix_df"
            ] = df

            st.session_state[
                "data_loaded"
            ] = True

            index_dataframe(df)

            st.success(
                f"Loaded {len(df)} rows"
            )

# ==========================================
# DATAFRAME
# ==========================================

df = st.session_state[
    "seat_matrix_df"
]

# ==========================================
# NO DATA
# ==========================================

if df.empty:

    st.warning(
        """
        Upload a KCET Seat Matrix PDF,
        CSV or Excel file to begin.
        """
    )

    st.stop()

# ==========================================
# SIDEBAR
# ==========================================

sidebar_data = render_sidebar(
    df
)

page = sidebar_data["page"]

filtered_df = sidebar_data[
    "filtered_df"
]

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

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(

    f"""
    Colleges:
    {filtered_df['college_name'].nunique()
    if 'college_name' in filtered_df.columns else 0}

    |
    Seats:
    {filtered_df['total_intake'].sum()
    if 'total_intake' in filtered_df.columns else 0:,}

    |
    Rows:
    {len(filtered_df):,}
    """
)

