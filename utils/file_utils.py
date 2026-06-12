"""
utils/file_utils.py

File Management Utilities
"""

import os
import json
import pandas as pd


def ensure_directory(path):

    os.makedirs(
        path,
        exist_ok=True
    )


def save_dataframe(
        df,
        filepath
):

    ensure_directory(
        os.path.dirname(filepath)
    )

    df.to_csv(
        filepath,
        index=False
    )


def load_dataframe(filepath):

    if os.path.exists(filepath):

        return pd.read_csv(
            filepath
        )

    return pd.DataFrame()


def save_json(
        data,
        filepath
):

    ensure_directory(
        os.path.dirname(filepath)
    )

    with open(
        filepath,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


def load_json(filepath):

    if not os.path.exists(filepath):
        return {}

    with open(
        filepath,
        "r"
    ) as f:

        return json.load(f)


def get_file_extension(path):

    return os.path.splitext(
        path
    )[1]


def is_pdf(path):

    return (
        get_file_extension(path)
        .lower()
        == ".pdf"
    )


def is_csv(path):

    return (
        get_file_extension(path)
        .lower()
        == ".csv"
    )


def list_files(directory):

    if not os.path.exists(directory):
        return []

    return [
        file
        for file in os.listdir(directory)
    ]


def delete_file(filepath):

    if os.path.exists(filepath):

        os.remove(filepath)
