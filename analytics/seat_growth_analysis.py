"""
analytics/seat_growth_analysis.py

Year Wise Growth Analytics
"""

import pandas as pd


class SeatGrowthAnalysis:

    def __init__(self, df):

        self.df = df

    def overall_growth(self):

        if "year" not in self.df.columns:
            return pd.DataFrame()

        return (
            self.df
            .groupby("year")
            ["total_intake"]
            .sum()
            .reset_index()
        )

    def college_growth(
        self,
        college_name
    ):

        if "year" not in self.df.columns:
            return pd.DataFrame()

        return (
            self.df[
                self.df["college_name"]
                == college_name
            ]
            .groupby("year")
            ["total_intake"]
            .sum()
            .reset_index()
        )

    def growth_percentage(
        self,
        college_name
    ):

        growth_df = (
            self.college_growth(
                college_name
            )
        )

        growth_df[
            "growth_percent"
        ] = (
            growth_df[
                "total_intake"
            ]
            .pct_change()
            * 100
        )

        return growth_df

    def highest_growth_colleges(
        self,
        top_n=10
    ):

        if "year" not in self.df.columns:
            return pd.DataFrame()

        result = []

        for college in self.df[
            "college_name"
        ].unique():

            college_df = (
                self.college_growth(
                    college
                )
            )

            if len(college_df) >= 2:

                growth = (
                    (
                        college_df[
                            "total_intake"
                        ].iloc[-1]
                        -
                        college_df[
                            "total_intake"
                        ].iloc[0]
                    )
                    /
                    college_df[
                        "total_intake"
                    ].iloc[0]
                ) * 100

                result.append({

                    "college_name":
                        college,

                    "growth_percent":
                        round(
                            growth,
                            2
                        )
                })

        return (
            pd.DataFrame(result)
            .sort_values(
                "growth_percent",
                ascending=False
            )
            .head(top_n)
        )
      
