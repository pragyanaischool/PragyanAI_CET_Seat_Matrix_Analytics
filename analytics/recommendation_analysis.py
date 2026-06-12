"""
analytics/recommendation_analysis.py

Recommendation Analytics
"""

import pandas as pd


class RecommendationAnalysis:

    def __init__(self, df):

        self.df = df

    def recommend_by_branch(
        self,
        branch,
        top_n=10
    ):

        result = self.df[
            self.df["course_name"]
            .str.contains(
                branch,
                case=False,
                na=False
            )
        ]

        return (
            result
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

    def recommend_by_district(
        self,
        district
    ):

        return self.df[
            self.df["district"]
            .str.contains(
                district,
                case=False,
                na=False
            )
        ]

    def recommend_ai_ml_colleges(
        self,
        top_n=20
    ):

        result = self.df[
            self.df["course_name"]
            .str.contains(
                "AI|ARTIFICIAL|MACHINE",
                case=False,
                na=False
            )
        ]

        return (
            result
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

    def recommend_by_rank(
        self,
        rank
    ):

        if rank <= 5000:

            category = "Dream"

        elif rank <= 25000:

            category = "Moderate"

        else:

            category = "Safe"

        return {

            "rank":
                rank,

            "category":
                category
        }

    def top_recommended(
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
