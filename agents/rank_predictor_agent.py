"""
agents/rank_predictor_agent.py
"""

import re


class RankPredictorAgent:

    def __init__(self):
        pass

    def category(
        self,
        rank
    ):

        if rank <= 5000:
            return "Dream"

        elif rank <= 25000:
            return "Moderate"

        else:
            return "Safe"

    def run(
        self,
        query
    ):

        match = re.search(
            r"\d+",
            query
        )

        if not match:

            return {
                "error":
                "Rank not found"
            }

        rank = int(
            match.group()
        )

        return {

            "rank":
                rank,

            "category":
                self.category(
                    rank
                )
        }
