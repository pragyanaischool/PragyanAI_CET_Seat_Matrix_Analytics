"""
research/nirf_scraper.py

NIRF Information Utility
"""

import pandas as pd


class NIRFScraper:

    def __init__(self):

        pass

    def get_nirf_info(
        self,
        college_name
    ):

        # Replace with actual NIRF source

        return {

            "college_name":
                college_name,

            "nirf_rank":
                "Not Available",

            "nirf_score":
                "Not Available",

            "category":
                "Engineering"
        }

    def rank_summary(
        self,
        college_name
    ):

        return self.get_nirf_info(
            college_name
        )
