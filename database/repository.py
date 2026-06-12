"""
database/repository.py

Repository Layer
"""

import json
import pandas as pd

from database.db import db


class CollegeRepository:

    # ==========================================
    # COLLEGES
    # ==========================================

    def insert_college(
        self,
        college
    ):

        query = """

        INSERT OR REPLACE INTO colleges (

            college_code,
            college_name,
            district,
            college_type,
            address,
            website,
            nirf_rank,
            naac_grade,
            placement_rate,
            highest_package,
            average_package,
            total_seats

        )

        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)

        """

        db.execute(

            query,

            (

                college.college_code,
                college.college_name,
                college.district,
                college.college_type,
                college.address,
                college.website,
                college.nirf_rank,
                college.naac_grade,
                college.placement_rate,
                college.highest_package,
                college.average_package,
                college.total_seats
            )
        )

    def get_all_colleges(self):

        query = """

        SELECT *
        FROM colleges

        """

        rows = db.fetch_all(
            query
        )

        return rows

    def get_college(
        self,
        college_name
    ):

        query = """

        SELECT *
        FROM colleges

        WHERE college_name=?

        """

        return db.fetch_one(
            query,
            (college_name,)
        )


class SeatMatrixRepository:

    # ==========================================
    # INSERT DATAFRAME
    # ==========================================

    def insert_dataframe(
        self,
        df
    ):

        for _, row in df.iterrows():

            query = """

            INSERT INTO seat_matrix (

                year,
                college_code,
                college_name,
                district,
                course_code,
                course_name,
                total_intake,
                kea_seats,
                hk_seats,
                rk_seats,
                management_seats,
                govt_seats

            )

            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)

            """

            db.execute(

                query,

                (

                    row.get("year"),

                    row.get("college_code"),

                    row.get("college_name"),

                    row.get("district"),

                    row.get("course_code"),

                    row.get("course_name"),

                    row.get("total_intake"),

                    row.get("kea_seats"),

                    row.get("hk_seats"),

                    row.get("rk_seats"),

                    row.get("management_seats"),

                    row.get("govt_seats")
                )
            )

    def get_year_data(
        self,
        year
    ):

        query = """

        SELECT *
        FROM seat_matrix

        WHERE year=?

        """

        rows = db.fetch_all(
            query,
            (year,)
        )

        return rows

    def get_all_data(self):

        query = """

        SELECT *
        FROM seat_matrix

        """

        rows = db.fetch_all(
            query
        )

        return rows


class AnalyticsRepository:

    def save_analysis(
        self,
        analysis_type,
        payload
    ):

        query = """

        INSERT INTO analytics (

            analysis_type,
            payload

        )

        VALUES (?,?)

        """

        db.execute(

            query,

            (

                analysis_type,

                json.dumps(payload)
            )
        )

    def get_analytics(self):

        query = """

        SELECT *
        FROM analytics

        """

        return db.fetch_all(
            query
        )


class ChatRepository:

    def save_chat(
        self,
        question,
        answer
    ):

        query = """

        INSERT INTO chat_history (

            question,
            answer

        )

        VALUES (?,?)

        """

        db.execute(

            query,

            (

                question,
                answer
            )
        )

    def get_history(self):

        query = """

        SELECT *

        FROM chat_history

        ORDER BY id DESC

        """

        return db.fetch_all(
            query
        )


class UserPreferenceRepository:

    def save_preference(
        self,
        rank,
        branch,
        district,
        category
    ):

        query = """

        INSERT INTO user_preferences (

            rank,
            preferred_branch,
            preferred_district,
            category

        )

        VALUES (?,?,?,?)

        """

        db.execute(

            query,

            (

                rank,
                branch,
                district,
                category
            )
        )

    def get_preferences(self):

        query = """

        SELECT *

        FROM user_preferences

        """

        return db.fetch_all(
            query
        )
