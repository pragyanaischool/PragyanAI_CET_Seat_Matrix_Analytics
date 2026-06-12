# ui/components/cards.py

import streamlit as st


def info_card(
        title,
        value
):

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:20px;
            border-radius:15px;
            box-shadow:0 3px 10px rgba(0,0,0,.1);
        ">
            <h4>{title}</h4>
            <h2>{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


def success_card(message):

    st.success(message)


def warning_card(message):

    st.warning(message)


def error_card(message):

    st.error(message)
