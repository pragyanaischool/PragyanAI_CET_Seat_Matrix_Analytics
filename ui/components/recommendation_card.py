# ui/components/recommendation_card.py

import streamlit as st


def recommendation_card(
        college_name,
        branch,
        reason,
        confidence
):

    st.markdown(
        f"""
        <div style="
            background:#ecfdf5;
            padding:20px;
            border-radius:15px;
            border-left:5px solid green;
            margin-bottom:15px;
        ">

        <h3>🎯 {college_name}</h3>

        <b>Branch:</b> {branch}<br>

        <b>Reason:</b> {reason}<br>

        <b>Confidence:</b> {confidence}%<br>

        </div>
        """,
        unsafe_allow_html=True
    )
