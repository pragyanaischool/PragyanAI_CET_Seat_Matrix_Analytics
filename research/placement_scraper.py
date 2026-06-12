"""
research/placement_scraper.py

Placement Information Utility
"""


class PlacementScraper:

    def __init__(self):
        pass

    def get_placement_info(
        self,
        college_name
    ):

        return {

            "college_name":
                college_name,

            "highest_package":
                "N/A",

            "average_package":
                "N/A",

            "placement_rate":
                "N/A",

            "top_recruiters": []
        }

    def placement_summary(
        self,
        college_name
    ):

        return self.get_placement_info(
            college_name
        )
