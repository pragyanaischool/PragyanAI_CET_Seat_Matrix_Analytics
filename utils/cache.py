"""
utils/cache.py

Caching Utilities
"""

import streamlit as st
import pandas as pd


@st.cache_data
def load_csv(path):

    return pd.read_csv(path)


@st.cache_data
def load_excel(path):

    return pd.read_excel(path)


@st.cache_resource
def load_vector_store(vdb):

    return vdb


@st.cache_data
def get_unique_colleges(df):

    return sorted(
        df["college_name"]
        .dropna()
        .unique()
    )


@st.cache_data
def get_unique_districts(df):

    return sorted(
        df["district"]
        .dropna()
        .unique()
    )
