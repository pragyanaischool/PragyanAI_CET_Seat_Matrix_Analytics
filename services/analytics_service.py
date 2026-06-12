"""
services/analytics_service.py

Analytics Business Logic
"""

import pandas as pd


class AnalyticsService:

    def __init__(self, df):

        self.df = df

    def total_colleges(self):

        return (
            self.df["college_name"]
            .nunique()
        )

    def total_seats(self):

        return int(
            self.df["total_intake"]
            .sum()
        )

    def total_branches(self):

        return (
            self.df["course_name"]
            .nunique()
        )

    def total_districts(self):

        return (
            self.df["district"]
            .nunique()
        )

    def district_wise_seats(self):

        return (
            self.df.groupby(
                "district"
            )["total_intake"]
            .sum()
            .reset_index()
        )

    def branch_wise_seats(self):

        return (
            self.df.groupby(
                "course_name"
            )["total_intake"]
            .sum()
            .reset_index()
        )

    def top_colleges(
        self,
        top_n=20
    ):

        return (
            self.df.groupby(
                "college_name"
            )["total_intake"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(top_n)
            .reset_index()
        )

    def year_wise_growth(self):

        if "year" not in self.df.columns:
            return pd.DataFrame()

        return (
            self.df.groupby(
                "year"
            )["total_intake"]
            .sum()
            .reset_index()
        )

    def district_wise_colleges(self):

        return (
            self.df.groupby(
                "district"
            )["college_name"]
            .nunique()
            .reset_index()
        )
