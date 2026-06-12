"""
rag/embeddings.py

Embedding Manager
"""

from sentence_transformers import (
    SentenceTransformer
)

from config.settings import (
    settings
)


class EmbeddingManager:

    def __init__(
        self,
        model_name="all-MiniLM-L6-v2"
    ):

        self.model = (
            SentenceTransformer(
                model_name
            )
        )

    def embed_text(
        self,
        text
    ):

        return self.model.encode(
            text
        ).tolist()

    def embed_documents(
        self,
        documents
    ):

        return self.model.encode(
            documents
        ).tolist()


embedding_manager = (
    EmbeddingManager()
)
