"""
extraction/seat_matrix_parser.py

KCET Seat Matrix Parser
"""

import re
import pandas as pd


class SeatMatrixParser:

    def __init__(self):
        pass

    def clean_dataframe(
        self,
        df
    ):

        df.columns = [

            str(col)
            .strip()
            .lower()
            .replace(" ", "_")

            for col in df.columns
        ]

        return df

    def standardize_columns(
        self,
        df
    ):

        mapping = {

            "college":
                "college_name",

            "college_code":
                "college_code",

            "branch":
                "course_name",

            "course":
                "course_name",

            "intake":
                "total_intake",

            "seats":
                "total_intake"
        }

        for old, new in mapping.items():

            if old in df.columns:

                df.rename(
                    columns={
                        old: new
                    },
                    inplace=True
                )

        return df

    def parse(
        self,
        df,
        year=None
    ):

        df = self.clean_dataframe(
            df
        )

        df = self.standardize_columns(
            df
        )

        if year:

            df["year"] = year

        return df

    def merge_years(
        self,
        dfs
    ):

        return pd.concat(
            dfs,
            ignore_index=True
        )
