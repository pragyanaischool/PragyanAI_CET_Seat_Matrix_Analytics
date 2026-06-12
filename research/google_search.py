"""
research/google_search.py

Google Search Utility
"""

import requests
from bs4 import BeautifulSoup


class GoogleSearch:

    def __init__(self):

        self.headers = {

            "User-Agent":
                "Mozilla/5.0"
        }

    def search(
        self,
        query
    ):

        url = (
            f"https://www.google.com/search?q={query}"
        )

        response = requests.get(
            url,
            headers=self.headers
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        results = []

        for link in soup.select("a"):

            href = link.get("href")

            if href:

                results.append(href)

        return results[:20]

    def search_college(
        self,
        college_name
    ):

        query = f"{college_name} official website"

        return self.search(query)
