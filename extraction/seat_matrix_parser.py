"""
extraction/seat_matrix_parser.py

Seat Matrix Parser
"""

import pandas as pd


class SeatMatrixParser:

    def __init__(self):

        self.column_mapping = {

            # College

            "College Name": "college_name",
            "College": "college_name",
            "COLLEGE NAME": "college_name",
            "college": "college_name",

            # District

            "District": "district",
            "DISTRICT": "district",

            # Course

            "Course Name": "course_name",
            "Course": "course_name",
            "Branch": "course_name",
            "BRANCH": "course_name",
            "Program": "course_name",

            # Intake

            "Intake": "total_intake",
            "Total Intake": "total_intake",
            "TOTAL INTAKE": "total_intake",
            "Seats": "total_intake",

            # Codes

            "College Code": "college_code",
            "COLLEGE CODE": "college_code",

            "Course Code": "course_code",
            "Branch Code": "course_code",

            # Year

            "Year": "year",
            "YEAR": "year"
        }

    # =====================================
    # MAIN PARSER
    # =====================================

    def parse(
        self,
        df
    ):

        if df is None:

            return pd.DataFrame()

        if df.empty:

            return pd.DataFrame()

        df = df.copy()

        df = self.clean_columns(df)

        df = self.rename_columns(df)

        df = self.ensure_required_columns(df)

        df = self.clean_values(df)

        return df

    # =====================================
    # CLEAN COLUMN NAMES
    # =====================================

    def clean_columns(
        self,
        df
    ):

        df.columns = [

            str(col).strip()

            for col in df.columns

        ]

        return df

    # =====================================
    # RENAME
    # =====================================

    def rename_columns(
        self,
        df
    ):

        rename_dict = {}

        for col in df.columns:

            if col in self.column_mapping:

                rename_dict[col] = (
                    self.column_mapping[col]
                )

            else:

                rename_dict[col] = (

                    str(col)
                    .lower()
                    .strip()
                    .replace(" ", "_")
                )

        df.rename(

            columns=rename_dict,

            inplace=True

        )

        return df

    # =====================================
    # REQUIRED COLUMNS
    # =====================================

    def ensure_required_columns(
        self,
        df
    ):

        required_columns = {

            "college_name": "",

            "district": "",

            "course_name": "",

            "total_intake": 0,

            "college_code": "",

            "course_code": "",

            "year": None
        }

        for column, default_value in (

            required_columns.items()

        ):

            if column not in df.columns:

                df[column] = default_value

        return df

    # =====================================
    # CLEAN VALUES
    # =====================================

    def clean_values(
        self,
        df
    ):

        text_columns = [

            "college_name",

            "district",

            "course_name",

            "college_code",

            "course_code"
        ]

        for col in text_columns:

            if col in df.columns:

                df[col] = (

                    df[col]

                    .astype(str)

                    .fillna("")

                    .str.strip()
                )

        if "total_intake" in df.columns:

            df["total_intake"] = pd.to_numeric(

                df["total_intake"],

                errors="coerce"

            ).fillna(0)

        if "year" in df.columns:

            df["year"] = pd.to_numeric(

                df["year"],

                errors="coerce"

            )

        return df

    # =====================================
    # DATASET SUMMARY
    # =====================================

    def summary(
        self,
        df
    ):

        return {

            "rows":
                len(df),

            "colleges":
                df["college_name"]
                .nunique()

                if "college_name"
                in df.columns

                else 0,

            "branches":
                df["course_name"]
                .nunique()

                if "course_name"
                in df.columns

                else 0,

            "districts":
                df["district"]
                .nunique()

                if "district"
                in df.columns

                else 0,

            "total_seats":
                int(
                    df["total_intake"]
                    .sum()
                )

                if "total_intake"
                in df.columns

                else 0
        }


# ==========================================
# SINGLETON
# ==========================================

seat_matrix_parser = (
    SeatMatrixParser()
)

