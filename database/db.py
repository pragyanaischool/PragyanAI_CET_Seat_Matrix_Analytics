"""
database/db.py

Database Connection Manager
"""

import sqlite3
from pathlib import Path

from database.schema import (
    COLLEGE_TABLE,
    SEAT_MATRIX_TABLE,
    ANALYTICS_TABLE,
    CHAT_HISTORY_TABLE,
    USER_PREFERENCES_TABLE
)


class Database:

    def __init__(
        self,
        db_path="data/cet.db"
    ):

        self.db_path = db_path

        Path(
            "data"
        ).mkdir(
            exist_ok=True
        )

        self.conn = sqlite3.connect(
            self.db_path,
            check_same_thread=False
        )

        self.create_tables()

    def create_tables(self):

        cursor = self.conn.cursor()

        cursor.execute(
            COLLEGE_TABLE
        )

        cursor.execute(
            SEAT_MATRIX_TABLE
        )

        cursor.execute(
            ANALYTICS_TABLE
        )

        cursor.execute(
            CHAT_HISTORY_TABLE
        )

        cursor.execute(
            USER_PREFERENCES_TABLE
        )

        self.conn.commit()

    def execute(
        self,
        query,
        params=None
    ):

        cursor = self.conn.cursor()

        if params:

            cursor.execute(
                query,
                params
            )

        else:

            cursor.execute(
                query
            )

        self.conn.commit()

        return cursor

    def fetch_all(
        self,
        query,
        params=None
    ):

        cursor = self.execute(
            query,
            params
        )

        return cursor.fetchall()

    def fetch_one(
        self,
        query,
        params=None
    ):

        cursor = self.execute(
            query,
            params
        )

        return cursor.fetchone()

    def close(self):

        self.conn.close()


db = Database()
