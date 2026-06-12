# ui/components/college_card.py

import streamlit as st


def college_card(
        name,
        district,
        seats,
        branches,
        college_type
):

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:20px;
            border-radius:15px;
            margin-bottom:10px;
            box-shadow:0 3px 10px rgba(0,0,0,.08);
        ">

        <h3>🏫 {name}</h3>

        <p>
        📍 {district}<br>
        🎓 Seats: {seats}<br>
        📚 Branches: {branches}<br>
        🏛 Type: {college_type}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )
