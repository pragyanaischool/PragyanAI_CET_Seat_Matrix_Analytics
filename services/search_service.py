"""
services/search_service.py

Search Layer
"""

import pandas as pd


class SearchService:

    def __init__(self, df):

        self.df = df

    def search_college(
        self,
        keyword
    ):

        return self.df[
            self.df["college_name"]
            .str.contains(
                keyword,
                case=False,
                na=False
            )
        ]

    def search_branch(
        self,
        branch
    ):

        return self.df[
            self.df["course_name"]
            .str.contains(
                branch,
                case=False,
                na=False
            )
        ]

    def search_district(
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

    def global_search(
        self,
        keyword
    ):

        return self.df[
            (
                self.df["college_name"]
                .astype(str)
                .str.contains(
                    keyword,
                    case=False,
                    na=False
                )
            )
            |
            (
                self.df["course_name"]
                .astype(str)
                .str.contains(
                    keyword,
                    case=False,
                    na=False
                )
            )
        ]
