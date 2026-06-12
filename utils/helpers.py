"""
utils/helpers.py

Common Helper Functions
"""

from datetime import datetime
import pandas as pd


def safe_int(value, default=0):
    try:
        return int(value)
    except:
        return default


def safe_float(value, default=0.0):
    try:
        return float(value)
    except:
        return default


def current_timestamp():
    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def format_number(value):

    try:
        return f"{int(value):,}"
    except:
        return str(value)


def percentage_change(old, new):

    if old == 0:
        return 0

    return round(
        ((new - old) / old) * 100,
        2
    )


def dataframe_summary(df):

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values":
            df.isnull().sum().sum()
    }


def remove_duplicates(df):

    return df.drop_duplicates()


def normalize_column_names(df):

    df.columns = [
        col.lower()
        .strip()
        .replace(" ", "_")
        for col in df.columns
    ]

    return df
def normalize_columns(df):

    mapping = {

        "College Name": "college_name",
        "College": "college_name",

        "District": "district",

        "Branch": "course_name",
        "Course Name": "course_name",

        "Total Intake": "total_intake",
        "Intake": "total_intake",

        "Year": "year"
    }

    df = df.rename(
        columns=mapping
    )

    df.columns = [

        str(c)
        .lower()
        .strip()
        .replace(" ", "_")

        for c in df.columns
    ]

    return df
