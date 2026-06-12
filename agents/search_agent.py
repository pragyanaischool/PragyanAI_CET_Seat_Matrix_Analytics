"""
agents/search_agent.py
"""

from services.search_service import (
    SearchService
)


class SearchAgent:

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
                "Data not loaded"
            }

        search_service = (
            SearchService(
                self.df
            )
        )

        result = (
            search_service
            .global_search(
                query
            )
        )

        return {

            "count":
                len(result),

            "results":
                result
                .head(20)
                .to_dict(
                    "records"
                )
        }
