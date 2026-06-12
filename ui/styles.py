"""
ui/styles.py
"""

import streamlit as st


def initialize_theme():
    """
    Minimal styling for the app.
    """

    st.markdown(
        """
        <style>

        .block-container {
            max-width: 1400px;
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        div[data-testid="metric-container"] {
            border-radius: 12px;
            padding: 12px;
            border: 1px solid rgba(128, 128, 128, 0.15);
        }

        .stButton > button {
            border-radius: 8px;
        }

        footer {
            visibility: hidden;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
    

