"""
agents/parser_agent.py

Query Parsing Agent
"""

import re


class ParserAgent:

    def __init__(self):
        pass

    def extract_rank(self, query):

        match = re.search(
            r"\b\d{3,6}\b",
            query
        )

        if match:
            return int(match.group())

        return None

    def extract_branch(self, query):

        branches = [

            "CSE",
            "ISE",
            "AI",
            "AI ML",
            "AIML",
            "ECE",
            "EEE",
            "MECHANICAL",
            "CIVIL"
        ]

        query_upper = query.upper()

        for branch in branches:

            if branch in query_upper:

                return branch

        return None

    def run(self, query):

        return {

            "query": query,

            "rank":
                self.extract_rank(
                    query
                ),

            "branch":
                self.extract_branch(
                    query
                )
        }
