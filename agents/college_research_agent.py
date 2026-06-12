"""
agents/college_research_agent.py
"""

from research.google_search import (
    GoogleSearch
)

from research.college_scraper import (
    CollegeScraper
)

from research.naac_scraper import (
    NAACScraper
)

from research.nirf_scraper import (
    NIRFScraper
)

from research.placement_scraper import (
    PlacementScraper
)


class CollegeResearchAgent:

    def __init__(self):

        self.google = (
            GoogleSearch()
        )

        self.scraper = (
            CollegeScraper()
        )

        self.naac = (
            NAACScraper()
        )

        self.nirf = (
            NIRFScraper()
        )

        self.placement = (
            PlacementScraper()
        )

    def run(
        self,
        college_name
    ):

        urls = (
            self.google
            .search_college(
                college_name
            )
        )

        return {

            "college":
                college_name,

            "search_results":
                urls[:10],

            "naac":
                self.naac
                .get_naac_info(
                    college_name
                ),

            "nirf":
                self.nirf
                .get_nirf_info(
                    college_name
                ),

            "placements":
                self.placement
                .get_placement_info(
                    college_name
                )
        }
