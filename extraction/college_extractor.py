"""
extraction/college_extractor.py

College Information Extraction
"""

import pandas as pd


class CollegeExtractor:

    def __init__(self):
        pass

    def extract_colleges(
        self,
        df
    ):

        if "college_name" not in df.columns:

            return pd.DataFrame()

        colleges = []

        grouped = df.groupby(
            "college_name"
        )

        for college, data in grouped:

            record = {

                "college_name":
                    college,

                "district":
                    (
                        data["district"]
                        .iloc[0]
                        if "district"
                        in data.columns
                        else None
                    ),

                "total_branches":
                    (
                        data["course_name"]
                        .nunique()
                        if "course_name"
                        in data.columns
                        else 0
                    ),

                "total_seats":
                    (
                        data["total_intake"]
                        .sum()
                        if "total_intake"
                        in data.columns
                        else 0
                    )
            }

            colleges.append(
                record
            )

        return pd.DataFrame(
            colleges
        )

    def extract_branches(
        self,
        df
    ):

        if "course_name" not in df.columns:

            return pd.DataFrame()

        return (
            df.groupby(
                "course_name"
            )["total_intake"]
            .sum()
            .reset_index()
            .sort_values(
                "total_intake",
                ascending=False
            )
        )

    def extract_district_summary(
        self,
        df
    ):

        if "district" not in df.columns:

            return pd.DataFrame()

        return (
            df.groupby(
                "district"
            )["total_intake"]
            .sum()
            .reset_index()
            .sort_values(
                "total_intake",
                ascending=False
            )
        )
