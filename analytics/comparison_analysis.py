"""
analytics/comparison_analysis.py

College Comparison Analytics
"""

import pandas as pd


class ComparisonAnalysis:

    def __init__(self, df):

        self.df = df

    def compare_colleges(
        self,
        college1,
        college2
    ):

        df1 = self.df[
            self.df["college_name"]
            == college1
        ]

        df2 = self.df[
            self.df["college_name"]
            == college2
        ]

        return {

            college1: {

                "seats":
                    int(
                        df1["total_intake"]
                        .sum()
                    ),

                "branches":
                    df1[
                        "course_name"
                    ].nunique()
            },

            college2: {

                "seats":
                    int(
                        df2["total_intake"]
                        .sum()
                    ),

                "branches":
                    df2[
                        "course_name"
                    ].nunique()
            }
        }

    def branch_comparison(
        self,
        college1,
        college2
    ):

        df1 = self.df[
            self.df["college_name"]
            == college1
        ]

        df2 = self.df[
            self.df["college_name"]
            == college2
        ]

        c1 = set(
            df1["course_name"]
        )

        c2 = set(
            df2["course_name"]
        )

        return {

            "common":
                list(
                    c1.intersection(c2)
                ),

            "college1_only":
                list(c1 - c2),

            "college2_only":
                list(c2 - c1)
        }
