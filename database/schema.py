"""
database/schema.py

Database Schema Definitions
"""

COLLEGE_TABLE = """

CREATE TABLE IF NOT EXISTS colleges (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    college_code TEXT UNIQUE,

    college_name TEXT,

    district TEXT,

    college_type TEXT,

    address TEXT,

    website TEXT,

    nirf_rank INTEGER,

    naac_grade TEXT,

    placement_rate REAL,

    highest_package REAL,

    average_package REAL,

    total_seats INTEGER,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

"""


SEAT_MATRIX_TABLE = """

CREATE TABLE IF NOT EXISTS seat_matrix (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    year INTEGER,

    college_code TEXT,

    college_name TEXT,

    district TEXT,

    course_code TEXT,

    course_name TEXT,

    total_intake INTEGER,

    kea_seats INTEGER,

    hk_seats INTEGER,

    rk_seats INTEGER,

    management_seats INTEGER,

    govt_seats INTEGER,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

"""


ANALYTICS_TABLE = """

CREATE TABLE IF NOT EXISTS analytics (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    analysis_type TEXT,

    payload TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

"""


CHAT_HISTORY_TABLE = """

CREATE TABLE IF NOT EXISTS chat_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    question TEXT,

    answer TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

"""


USER_PREFERENCES_TABLE = """

CREATE TABLE IF NOT EXISTS user_preferences (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    rank INTEGER,

    preferred_branch TEXT,

    preferred_district TEXT,

    category TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

"""
