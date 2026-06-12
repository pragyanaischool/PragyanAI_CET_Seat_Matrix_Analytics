"""
config/settings.py

Application Settings
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    # =====================================================
    # APP
    # =====================================================

    APP_NAME = "Smart CET AI Counsellor"

    VERSION = "1.0.0"

    DEBUG = True

    # =====================================================
    # PATHS
    # =====================================================

    BASE_DIR = os.getcwd()

    DATA_DIR = "data"

    RAW_DATA_DIR = "data/raw"

    PROCESSED_DATA_DIR = "data/processed"

    VECTOR_DB_DIR = "data/vector_db"

    LOG_DIR = "logs"

    # =====================================================
    # GROQ
    # =====================================================

    GROQ_API_KEY = os.getenv(
        "GROQ_API_KEY"
    )

    # =====================================================
    # CHROMADB
    # =====================================================

    CHROMA_DB_PATH = "data/vector_db"

    COLLECTION_NAME = (
        "college_knowledge_base"
    )

    # =====================================================
    # PDF EXTRACTION
    # =====================================================

    CHUNK_SIZE = 1000

    CHUNK_OVERLAP = 200

    # =====================================================
    # STREAMLIT
    # =====================================================

    PAGE_TITLE = (
        "Smart CET AI Counsellor"
    )

    PAGE_ICON = "🎓"

    LAYOUT = "wide"


settings = Settings()
