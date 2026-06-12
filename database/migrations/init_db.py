"""
database/migrations/init_db.py

Initialize Database
"""

from database.db import Database


def initialize():

    Database()

    print(
        "Database initialized successfully."
    )


if __name__ == "__main__":

    initialize()
