"""
llm/models.py

Model Registry
"""

MODELS = {

    "fast":
        "llama-3.1-8b-instant",

    "smart":
        "llama-3.3-70b-versatile",

    "reasoning":
        "deepseek-r1-distill-llama-70b"
}


def get_model(
    model_type="smart"
):

    return MODELS.get(
        model_type,
        MODELS["smart"]
    )
