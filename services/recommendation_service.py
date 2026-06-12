"""
services/recommendation_service.py

College Recommendation Engine
"""

import pandas as pd


class RecommendationService:

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
            result.groupby(
                "college_name"
            )["total_intake"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(top_n)
            .reset_index()
        )

    def recommend_by_district(
        self,
        district
    ):

        return self.df[
            self.df["district"]
            == district
        ]

    def recommend_by_rank(
        self,
        rank
    ):

        if rank <= 5000:

            return "Dream Colleges"

        elif rank <= 25000:

            return "Moderate Colleges"

        else:

            return "Safe Colleges"

    def recommend_top_ai_ml(
        self
    ):

        result = self.df[
            self.df["course_name"]
            .str.contains(
                "ARTIFICIAL",
                case=False,
                na=False
            )
        ]

        return (
            result.groupby(
                "college_name"
            )["total_intake"]
            .sum()
            .sort_values(
                ascending=False
            )
            .reset_index()
        )
