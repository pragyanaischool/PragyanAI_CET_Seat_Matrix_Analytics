"""
ui/styles.py

Minimal Professional Theme
"""

import streamlit as st

def initialize_theme():
"""
Apply minimal styling.
Streamlit theme controls colors.
"""

```
st.markdown(
    """
    <style>

    /* Main Container */

    .block-container {
        max-width: 1400px;
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    /* Metric Cards */

    div[data-testid="metric-container"] {
        border-radius: 12px;
        padding: 12px;
        border: 1px solid rgba(128,128,128,0.15);
    }

    /* Buttons */

    .stButton > button {
        border-radius: 8px;
    }

    /* Dataframes */

    .stDataFrame {
        border-radius: 10px;
    }

    /* Chat Messages */

    .stChatMessage {
        border-radius: 10px;
    }

    /* Hide Footer */

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)
```

