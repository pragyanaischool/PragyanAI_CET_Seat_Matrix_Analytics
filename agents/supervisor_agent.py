"""
agents/supervisor_agent.py

Agent Router
"""


class SupervisorAgent:

    def __init__(self):
        pass

    def route(
        self,
        query
    ):

        q = query.lower()

        if (
            "analytics" in q
            or "trend" in q
            or "growth" in q
        ):

            return "analytics"

        elif (
            "recommend" in q
            or "suggest" in q
        ):

            return "recommendation"

        elif (
            "placement" in q
            or "naac" in q
            or "nirf" in q
            or "college details" in q
        ):

            return "research"

        elif (
            "rank" in q
        ):

            return "rank"

        elif (
            "search" in q
        ):

            return "search"

        else:

            return "chatbot"

    def run(
        self,
        query
    ):

        return {

            "agent":
                self.route(
                    query
                )
        }
