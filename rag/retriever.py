"""
rag/retriever.py

Retriever Layer
"""

from rag.vectorstore import (
    vector_store
)


class CollegeRetriever:

    def __init__(self):

        self.store = (
            vector_store
        )

    def retrieve(
        self,
        query,
        top_k=5
    ):

        results = (
            self.store.similarity_search(
                query,
                top_k
            )
        )

        return results

    def get_context(
        self,
        query,
        top_k=5
    ):

        results = self.retrieve(
            query,
            top_k
        )

        docs = results.get(
            "documents",
            [[]]
        )[0]

        return "\n\n".join(
            docs
        )


retriever = (
    CollegeRetriever()
)
