"""
analytics/branch_analysis.py

Branch Analytics
"""

import pandas as pd


class BranchAnalysis:

    def __init__(self, df):

        self.df = df

    def branch_wise_seats(self):

        return (
            self.df
            .groupby("course_name")
            ["total_intake"]
            .sum()
            .reset_index()
            .sort_values(
                "total_intake",
                ascending=False
            )
        )

    def top_branches(
        self,
        top_n=15
    ):

        return (
            self.branch_wise_seats()
            .head(top_n)
        )

    def branch_college_count(self):

        return (
            self.df
            .groupby("course_name")
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

    def branch_summary(
        self,
        branch
    ):

        df = self.df[
            self.df["course_name"]
            == branch
        ]

        return {

            "branch":
                branch,

            "colleges":
                df["college_name"]
                .nunique(),

            "seats":
                int(
                    df["total_intake"]
                    .sum()
                )
        }
      
