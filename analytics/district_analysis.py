"""
analytics/district_analysis.py

District Analytics
"""

import pandas as pd


class DistrictAnalysis:

    def __init__(self, df):

        self.df = df

    def district_wise_seats(self):

        return (
            self.df
            .groupby("district")
            ["total_intake"]
            .sum()
            .reset_index()
            .sort_values(
                "total_intake",
                ascending=False
            )
        )

    def district_wise_colleges(self):

        return (
            self.df
            .groupby("district")
            ["college_name"]
            .nunique()
            .reset_index()
            .rename(
                columns={
                    "college_name":
                    "college_count"
                }
            )
        )

    def top_districts(
        self,
        top_n=10
    ):

        return (
            self.district_wise_seats()
            .head(top_n)
        )

    def district_summary(
        self,
        district
    ):

        df = self.df[
            self.df["district"]
            == district
        ]

        return {

            "district":
                district,

            "colleges":
                df["college_name"]
                .nunique(),

            "branches":
                df["course_name"]
                .nunique(),

            "seats":
                int(
                    df["total_intake"]
                    .sum()
                )
        }
