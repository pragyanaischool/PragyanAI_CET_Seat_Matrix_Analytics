"""
research/naac_scraper.py

NAAC Information Utility
"""


class NAACScraper:

    def __init__(self):
        pass

    def get_naac_info(
        self,
        college_name
    ):

        return {

            "college_name":
                college_name,

            "naac_grade":
                "Not Available",

            "cgpa":
                "Not Available"
        }

    def accreditation_summary(
        self,
        college_name
    ):

        return self.get_naac_info(
            college_name
        )
