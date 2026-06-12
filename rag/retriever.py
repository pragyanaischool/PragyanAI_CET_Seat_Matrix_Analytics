"""
rag/retriever.py

FAISS Retriever Layer
"""

from rag.vectorstore import (
    vector_store
)


class CollegeRetriever:
    """
    Retriever wrapper around FAISS Vector Store
    """

    def __init__(self):

        self.vector_store = (
            vector_store
        )

    # =====================================
    # RETRIEVE DOCUMENTS
    # =====================================

    def retrieve(
        self,
        query,
        top_k=5
    ):

        return (

            self.vector_store
            .similarity_search(
                query=query,
                top_k=top_k
            )

        )

    # =====================================
    # RETRIEVE WITH SCORES
    # =====================================

    def retrieve_with_scores(
        self,
        query,
        top_k=5
    ):

        return (

            self.vector_store
            .similarity_search_with_scores(
                query=query,
                top_k=top_k
            )

        )

    # =====================================
    # GET CONTEXT
    # =====================================

    def get_context(
        self,
        query,
        top_k=5
    ):

        docs = self.retrieve(
            query=query,
            top_k=top_k
        )

        if not docs:

            return ""

        return "\n\n".join(
            docs
        )

    # =====================================
    # GET CONTEXT WITH SCORES
    # =====================================

    def get_context_with_scores(
        self,
        query,
        top_k=5
    ):

        results = (
            self.retrieve_with_scores(
                query=query,
                top_k=top_k
            )
        )

        if not results:

            return []

        return results

    # =====================================
    # DEBUG SEARCH
    # =====================================

    def debug_search(
        self,
        query,
        top_k=5
    ):

        results = (
            self.retrieve_with_scores(
                query=query,
                top_k=top_k
            )
        )

        print("\n")
        print("=" * 60)
        print("QUERY")
        print("=" * 60)
        print(query)

        print("\n")
        print("=" * 60)
        print("RETRIEVED DOCUMENTS")
        print("=" * 60)

        for idx, item in enumerate(
            results,
            start=1
        ):

            print(
                f"\nResult {idx}"
            )

            print(
                f"Score: {item['score']}"
            )

            print(
                item["document"][:500]
            )

        return results

    # =====================================
    # DOCUMENT COUNT
    # =====================================

    def document_count(
        self
    ):

        return (
            self.vector_store
            .count()
        )

    # =====================================
    # STORE INFO
    # =====================================

    def info(
        self
    ):

        return (

            self.vector_store
            .info()

        )


# ==========================================
# SINGLETON INSTANCE
# ==========================================

retriever = (
    CollegeRetriever()
)

