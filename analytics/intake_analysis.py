"""
analytics/intake_analysis.py

College Intake Analytics
"""

import pandas as pd


class IntakeAnalysis:

    def __init__(self, df):

        self.df = df

    def top_colleges_by_intake(
        self,
        top_n=20
    ):

        return (
            self.df
            .groupby("college_name")
            ["total_intake"]
            .sum()
            .reset_index()
            .sort_values(
                "total_intake",
                ascending=False
            )
            .head(top_n)
        )

    def average_intake(self):

        return round(
            self.df
            .groupby("college_name")
            ["total_intake"]
            .sum()
            .mean(),
            2
        )

    def max_intake(self):

        return (
            self.df
            .groupby("college_name")
            ["total_intake"]
            .sum()
            .max()
        )

    def min_intake(self):

        return (
            self.df
            .groupby("college_name")
            ["total_intake"]
            .sum()
            .min()
        )

    def intake_distribution(self):

        return (
            self.df
            .groupby("college_name")
            ["total_intake"]
            .sum()
            .reset_index()
        )
