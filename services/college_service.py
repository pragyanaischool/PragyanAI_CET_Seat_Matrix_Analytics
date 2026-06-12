"""
services/college_service.py

College Business Logic Layer
"""

import pandas as pd


class CollegeService:

    def __init__(self, df):

        self.df = df

    def get_all_colleges(self):

        return sorted(
            self.df["college_name"]
            .dropna()
            .unique()
        )

    def get_college_details(
        self,
        college_name
    ):

        college_df = self.df[
            self.df["college_name"]
            == college_name
        ]

        if college_df.empty:
            return {}

        result = {

            "college_name":
                college_name,

            "district":
                college_df[
                    "district"
                ].iloc[0],

            "college_type":
                college_df.get(
                    "college_type",
                    pd.Series(["N/A"])
                ).iloc[0],

            "total_seats":
                int(
                    college_df[
                        "total_intake"
                    ].sum()
                ),

            "branches":
                list(
                    college_df[
                        "course_name"
                    ].unique()
                )
        }

        return result

    def get_college_branches(
        self,
        college_name
    ):

        college_df = self.df[
            self.df["college_name"]
            == college_name
        ]

        return list(
            college_df[
                "course_name"
            ].unique()
        )

    def get_college_seat_matrix(
        self,
        college_name
    ):

        return self.df[
            self.df["college_name"]
            == college_name
        ]

    def get_college_growth(
        self,
        college_name
    ):

        if "year" not in self.df.columns:
            return pd.DataFrame()

        return (
            self.df[
                self.df["college_name"]
                == college_name
            ]
            .groupby("year")
            ["total_intake"]
            .sum()
            .reset_index()
        )
