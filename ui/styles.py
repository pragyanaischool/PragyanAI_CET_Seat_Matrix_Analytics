"""
ui/styles.py

PragyanAI CET Seat Matrix Analytics
"""

import streamlit as st

def initialize_theme():
"""Apply custom application styling"""

```
st.markdown(
    """
    <style>

    .stApp {
        background-color: #F8FAFC;
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }

    h1 {
        color: #1E3A8A;
        font-weight: 700;
    }

    h2 {
        color: #2563EB;
        font-weight: 600;
    }

    h3 {
        color: #334155;
    }

    section[data-testid="stSidebar"] {
        background-color: #0F172A;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    div[data-testid="metric-container"] {
        background-color: white;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 12px;
    }

    .stButton > button {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #1D4ED8;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)
```

