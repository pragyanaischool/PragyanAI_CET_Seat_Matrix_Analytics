"""
database/migrations/reset_db.py
"""

import os


DB_PATH = "data/cet.db"


def reset_database():

    if os.path.exists(DB_PATH):

        os.remove(DB_PATH)

        print(
            "Database removed."
        )

    else:

        print(
            "Database not found."
        )


if __name__ == "__main__":

    reset_database()
