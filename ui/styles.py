"""
ui/styles.py

PragyanAI CET Analytics
Professional Streamlit Theme
"""

import streamlit as st

def initialize_theme():
"""Apply custom styling"""


st.markdown(
    """
    <style>

    /* =========================
       Main App
    ========================== */

    .stApp {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }

    /* =========================
       Sidebar
    ========================== */

    section[data-testid="stSidebar"] {
        background-color: #0f172a;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* =========================
       Headers
    ========================== */

    h1 {
        color: #1e3a8a;
        font-weight: 700;
    }

    h2 {
        color: #2563eb;
        font-weight: 600;
    }

    h3 {
        color: #334155;
    }

    /* =========================
       Metrics
    ========================== */

    div[data-testid="metric-container"] {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    /* =========================
       Buttons
    ========================== */

    .stButton > button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }

    /* =========================
       Tables
    ========================== */

    .stDataFrame {
        border-radius: 10px;
    }

    /* =========================
       Chat
    ========================== */

    .stChatMessage {
        border-radius: 10px;
    }

    /* =========================
       Hide Streamlit Footer
    ========================== */

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)
