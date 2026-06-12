"""
llm/structured_output.py

Structured Parsing Utilities
"""

import json


def extract_json(
    text
):

    try:

        start = text.find("{")

        end = text.rfind("}") + 1

        return json.loads(
            text[start:end]
        )

    except Exception:

        return {}
