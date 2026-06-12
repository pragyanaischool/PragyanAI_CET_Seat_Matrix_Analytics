# ui/components/chatbot_bubble.py

import streamlit as st


def user_message(text):

    st.markdown(
        f"""
        <div style="
            background:#2563eb;
            color:white;
            padding:12px;
            border-radius:12px;
            margin-bottom:8px;
            text-align:right;
        ">
        {text}
        </div>
        """,
        unsafe_allow_html=True
    )


def assistant_message(text):

    st.markdown(
        f"""
        <div style="
            background:#f1f5f9;
            color:black;
            padding:12px;
            border-radius:12px;
            margin-bottom:8px;
        ">
        {text}
        </div>
        """,
        unsafe_allow_html=True
    )
