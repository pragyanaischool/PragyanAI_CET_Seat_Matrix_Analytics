"""
research/college_scraper.py

College Website Scraper
"""

import requests
from bs4 import BeautifulSoup


class CollegeScraper:

    def scrape(
        self,
        website_url
    ):

        try:

            response = requests.get(
                website_url,
                timeout=20
            )

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            title = (
                soup.title.text
                if soup.title
                else ""
            )

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            return {

                "title": title,

                "content": text[:10000]
            }

        except Exception as e:

            return {

                "error": str(e)
            }

    def extract_about(
        self,
        website_url
    ):

        data = self.scrape(
            website_url
        )

        return data.get(
            "content",
            ""
        )[:3000]
