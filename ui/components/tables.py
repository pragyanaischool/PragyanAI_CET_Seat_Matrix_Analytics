# ui/components/tables.py

import streamlit as st


def show_dataframe(df):

    st.dataframe(
        df,
        use_container_width=True
    )


def show_seat_matrix(df):

    st.subheader(
        "Seat Matrix"
    )

    st.dataframe(
        df,
        use_container_width=True
    )


def show_top_colleges(df):

    st.dataframe(
        df.head(20),
        use_container_width=True
    )
