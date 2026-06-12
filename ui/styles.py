# ui/styles.py

"""
Professional Streamlit Styling
Smart CET AI Counsellor

Author: PragyanAI
"""

import streamlit as st


# ==========================================================
# PAGE CONFIG
# ==========================================================

def configure_page():

    st.set_page_config(
        page_title="Smart CET AI Counsellor",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded"
    )


# ==========================================================
# GLOBAL CSS
# ==========================================================

def load_css():

    st.markdown(
        """
<style>

/* =====================================================
IMPORT FONT
===================================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}


/* =====================================================
APP BACKGROUND
===================================================== */

.stApp {

    background-color: #F8FAFC;

}


/* =====================================================
MAIN CONTAINER
===================================================== */

.block-container {

    padding-top: 1rem;
    padding-bottom: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}


/* =====================================================
SIDEBAR
===================================================== */

[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #0F172A,
        #1E293B
    );

    border-right: 1px solid #334155;
}

[data-testid="stSidebar"] * {

    color: white !important;

}


/* =====================================================
SIDEBAR TITLE
===================================================== */

.sidebar-title {

    text-align: center;

    font-size: 24px;

    font-weight: bold;

    margin-bottom: 20px;
}


/* =====================================================
PAGE TITLE
===================================================== */

.main-title {

    font-size: 42px;

    font-weight: 700;

    color: #0F172A;

    margin-bottom: 10px;
}


/* =====================================================
PAGE SUBTITLE
===================================================== */

.sub-title {

    color: #64748B;

    font-size: 18px;

    margin-bottom: 30px;
}


/* =====================================================
METRIC CARDS
===================================================== */

.metric-card {

    background: white;

    padding: 20px;

    border-radius: 16px;

    box-shadow:
        0px 4px 15px
        rgba(0,0,0,0.08);

    border: 1px solid #E2E8F0;
}


/* =====================================================
COLLEGE CARD
===================================================== */

.college-card {

    background: white;

    padding: 20px;

    border-radius: 16px;

    margin-bottom: 15px;

    border: 1px solid #E2E8F0;

    box-shadow:
        0px 4px 10px
        rgba(0,0,0,0.05);
}


/* =====================================================
SUCCESS CARD
===================================================== */

.success-card {

    background: #ECFDF5;

    padding: 15px;

    border-radius: 12px;

    border-left: 6px solid #10B981;
}


/* =====================================================
WARNING CARD
===================================================== */

.warning-card {

    background: #FFF7ED;

    padding: 15px;

    border-radius: 12px;

    border-left: 6px solid #F97316;
}


/* =====================================================
INFO CARD
===================================================== */

.info-card {

    background: #EFF6FF;

    padding: 15px;

    border-radius: 12px;

    border-left: 6px solid #3B82F6;
}


/* =====================================================
CHAT USER
===================================================== */

.chat-user {

    background: #2563EB;

    color: white;

    padding: 12px;

    border-radius: 12px;

    margin-bottom: 10px;
}


/* =====================================================
CHAT ASSISTANT
===================================================== */

.chat-assistant {

    background: #F1F5F9;

    color: black;

    padding: 12px;

    border-radius: 12px;

    margin-bottom: 10px;
}


/* =====================================================
BUTTONS
===================================================== */

.stButton > button {

    width: 100%;

    background-color: #2563EB;

    color: white;

    border-radius: 10px;

    border: none;

    padding: 12px;

    font-weight: 600;
}

.stButton > button:hover {

    background-color: #1D4ED8;

    color: white;
}


/* =====================================================
DOWNLOAD BUTTON
===================================================== */

.stDownloadButton > button {

    width: 100%;

    background-color: #16A34A;

    color: white;

    border-radius: 10px;

    border: none;
}


/* =====================================================
INPUTS
===================================================== */

.stTextInput input {

    border-radius: 10px;
}

.stSelectbox div {

    border-radius: 10px;
}

.stMultiSelect div {

    border-radius: 10px;
}


/* =====================================================
FILE UPLOADER
===================================================== */

[data-testid="stFileUploader"] {

    background: white;

    padding: 15px;

    border-radius: 12px;

    border: 1px solid #CBD5E1;
}


/* =====================================================
TABS
===================================================== */

button[data-baseweb="tab"] {

    font-size: 15px;

    font-weight: 600;
}


/* =====================================================
DATAFRAME
===================================================== */

[data-testid="stDataFrame"] {

    border-radius: 12px;

    overflow: hidden;

    border: 1px solid #E2E8F0;
}


/* =====================================================
EXPANDER
===================================================== */

.streamlit-expanderHeader {

    font-weight: 600;
}


/* =====================================================
SCROLLBAR
===================================================== */

::-webkit-scrollbar {

    width: 10px;
}

::-webkit-scrollbar-track {

    background: #CBD5E1;
}

::-webkit-scrollbar-thumb {

    background: #2563EB;

    border-radius: 10px;
}


/* =====================================================
FOOTER
===================================================== */

.footer {

    margin-top: 50px;

    text-align: center;

    color: #64748B;

    font-size: 14px;
}


/* =====================================================
HIDE STREAMLIT DEFAULTS
===================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# PAGE HEADER
# ==========================================================

def render_header():

    st.markdown(
        """
        <div class='main-title'>
            🎓 Smart CET AI Counsellor
        </div>

        <div class='sub-title'>
            Karnataka College Intelligence Platform
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# FOOTER
# ==========================================================

def render_footer():

    st.markdown(
        """
        <div class='footer'>
            Built using Streamlit • LangChain • LangGraph • Groq • ChromaDB
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# CARD COMPONENT
# ==========================================================

def info_card(title, value):

    st.markdown(
        f"""
        <div class="college-card">
            <h4>{title}</h4>
            <h2>{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# SUCCESS BOX
# ==========================================================

def success_box(message):

    st.markdown(
        f"""
        <div class="success-card">
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# WARNING BOX
# ==========================================================

def warning_box(message):

    st.markdown(
        f"""
        <div class="warning-card">
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# INFO BOX
# ==========================================================

def info_box(message):

    st.markdown(
        f"""
        <div class="info-card">
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# INITIALIZE THEME
# ==========================================================

def initialize_theme():

    configure_page()

    load_css()


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    initialize_theme()

    render_header()

    info_card(
        "Total Colleges",
        "245"
    )

    success_box(
        "Analytics Engine Loaded Successfully"
    )

    warning_box(
        "Seat Matrix Not Uploaded"
    )

    info_box(
        "Upload PDFs to begin analysis."
    )

    render_footer()
