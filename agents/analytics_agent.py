"""
agents/analytics_agent.py
"""

from analytics.intake_analysis import (
    IntakeAnalysis
)

from analytics.branch_analysis import (
    BranchAnalysis
)

from analytics.district_analysis import (
    DistrictAnalysis
)


class AnalyticsAgent:

    def __init__(
        self,
        dataframe=None
    ):

        self.df = dataframe

    def run(
        self,
        query
    ):

        if self.df is None:

            return {
                "error":
                "DataFrame not loaded"
            }

        return {

            "top_colleges":
                IntakeAnalysis(
                    self.df
                ).top_colleges_by_intake(),

            "top_branches":
                BranchAnalysis(
                    self.df
                ).top_branches(),

            "top_districts":
                DistrictAnalysis(
                    self.df
                ).top_districts()
        }
