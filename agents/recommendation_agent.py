"""
agents/recommendation_agent.py
"""

from analytics.recommendation_analysis import (
    RecommendationAnalysis
)


class RecommendationAgent:

    def __init__(
        self,
        dataframe=None
    ):

        self.df = dataframe

    def run(
        self,
        query
    ):

        if self.df is None:

            return {
                "error":
                "No data loaded"
            }

        recommender = (
            RecommendationAnalysis(
                self.df
            )
        )

        if "ai" in query.lower():

            return (
                recommender
                .recommend_ai_ml_colleges()
                .head(10)
                .to_dict(
                    "records"
                )
            )

        return (
            recommender
            .top_recommended()
            .head(10)
            .to_dict(
                "records"
            )
        )
