"""
services/chat_service.py

Chat Business Logic
"""

from services.analytics_service import (
    AnalyticsService
)

from services.college_service import (
    CollegeService
)


class ChatService:

    def __init__(
        self,
        df,
        llm=None
    ):

        self.df = df
        self.llm = llm

        self.analytics = (
            AnalyticsService(df)
        )

        self.college_service = (
            CollegeService(df)
        )

    def get_context(self):

        return f"""

        Total Colleges:
        {self.analytics.total_colleges()}

        Total Seats:
        {self.analytics.total_seats()}

        Total Branches:
        {self.analytics.total_branches()}

        """

    def generate_response(
        self,
        query
    ):

        if self.llm is None:

            return (
                "LLM not configured."
            )

        prompt = f"""

        You are a KCET College Counsellor.

        Dataset Context:

        {self.get_context()}

        User Question:

        {query}

        """

        response = self.llm.invoke(
            prompt
        )

        return response

    def simple_response(
        self,
        query
    ):

        q = query.lower()

        if "total colleges" in q:

            return (
                f"Total Colleges: "
                f"{self.analytics.total_colleges()}"
            )

        if "total seats" in q:

            return (
                f"Total Seats: "
                f"{self.analytics.total_seats()}"
            )

        if "top college" in q:

            top = (
                self.analytics
                .top_colleges(1)
            )

            return (
                top.iloc[0]
                ["college_name"]
            )

        return (
            "Please ask about colleges, "
            "seats, branches or districts."
        )
