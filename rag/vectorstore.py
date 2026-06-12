"""
rag/vectorstore.py

ChromaDB Vector Store
"""

import chromadb

from chromadb.config import (
    Settings as ChromaSettings
)

from config.settings import (
    settings
)

from rag.embeddings import (
    embedding_manager
)


class CollegeVectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_DB_PATH
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=settings.COLLECTION_NAME
            )
        )

    def add_documents(
        self,
        texts,
        metadatas=None
    ):

        embeddings = (
            embedding_manager
            .embed_documents(
                texts
            )
        )

        ids = [

            f"doc_{i}"

            for i in range(
                len(texts)
            )
        ]

        self.collection.add(

            ids=ids,

            documents=texts,

            embeddings=embeddings,

            metadatas=metadatas
        )

    def similarity_search(
        self,
        query,
        top_k=5
    ):

        query_embedding = (
            embedding_manager
            .embed_text(
                query
            )
        )

        result = (
            self.collection.query(
                query_embeddings=[
                    query_embedding
                ],
                n_results=top_k
            )
        )

        return result

    def count(self):

        return self.collection.count()


vector_store = (
    CollegeVectorStore()
)
