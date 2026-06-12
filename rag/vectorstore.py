"""
rag/vectorstore.py

FAISS Vector Store for CET Analytics
"""

import os
import json
import faiss
import numpy as np

from sentence_transformers import (
    SentenceTransformer
)


class FAISSVectorStore:

    def __init__(
        self,
        model_name="all-MiniLM-L6-v2",
        index_path="data/vector_db/faiss.index",
        metadata_path="data/vector_db/documents.json"
    ):

        self.model_name = model_name

        self.index_path = index_path

        self.metadata_path = metadata_path

        os.makedirs(
            "data/vector_db",
            exist_ok=True
        )

        self.model = (
            SentenceTransformer(
                model_name
            )
        )

        self.dimension = (
            self.model
            .get_sentence_embedding_dimension()
        )

        self.documents = []

        self.index = (
            faiss.IndexFlatL2(
                self.dimension
            )
        )

        self._load()

    # =====================================
    # EMBEDDINGS
    # =====================================

    def embed(
        self,
        texts
    ):

        if isinstance(
            texts,
            str
        ):

            texts = [texts]

        embeddings = (
            self.model.encode(
                texts,
                convert_to_numpy=True
            )
        )

        return np.array(
            embeddings,
            dtype=np.float32
        )

    # =====================================
    # ADD DOCUMENTS
    # =====================================

    def add_documents(
        self,
        documents
    ):

        if not documents:

            return

        embeddings = self.embed(
            documents
        )

        self.index.add(
            embeddings
        )

        self.documents.extend(
            documents
        )

        self.save()

    # =====================================
    # SEARCH
    # =====================================

    def similarity_search(
        self,
        query,
        top_k=5
    ):

        if len(
            self.documents
        ) == 0:

            return []

        query_embedding = (
            self.embed(
                query
            )
        )

        distances, indices = (
            self.index.search(
                query_embedding,
                min(
                    top_k,
                    len(
                        self.documents
                    )
                )
            )
        )

        results = []

        for idx in indices[0]:

            if (
                idx >= 0
                and idx < len(
                    self.documents
                )
            ):

                results.append(

                    self.documents[idx]

                )

        return results

    # =====================================
    # SEARCH WITH SCORES
    # =====================================

    def similarity_search_with_scores(
        self,
        query,
        top_k=5
    ):

        if len(
            self.documents
        ) == 0:

            return []

        query_embedding = (
            self.embed(
                query
            )
        )

        distances, indices = (
            self.index.search(
                query_embedding,
                min(
                    top_k,
                    len(
                        self.documents
                    )
                )
            )
        )

        results = []

        for score, idx in zip(

            distances[0],
            indices[0]

        ):

            if (
                idx >= 0
                and idx < len(
                    self.documents
                )
            ):

                results.append(

                    {

                        "document":
                            self.documents[idx],

                        "score":
                            float(score)
                    }

                )

        return results

    # =====================================
    # COUNT
    # =====================================

    def count(
        self
    ):

        return len(
            self.documents
        )

    # =====================================
    # CLEAR
    # =====================================

    def clear(
        self
    ):

        self.documents = []

        self.index = (
            faiss.IndexFlatL2(
                self.dimension
            )
        )

        self.save()

    # =====================================
    # SAVE
    # =====================================

    def save(
        self
    ):

        try:

            faiss.write_index(

                self.index,

                self.index_path

            )

            with open(

                self.metadata_path,

                "w",

                encoding="utf-8"

            ) as f:

                json.dump(

                    self.documents,

                    f,

                    ensure_ascii=False,

                    indent=2

                )

        except Exception as e:

            print(
                f"FAISS Save Error: {e}"
            )

    # =====================================
    # LOAD
    # =====================================

    def _load(
        self
    ):

        try:

            if os.path.exists(
                self.index_path
            ):

                self.index = (
                    faiss.read_index(
                        self.index_path
                    )
                )

            if os.path.exists(
                self.metadata_path
            ):

                with open(

                    self.metadata_path,

                    "r",

                    encoding="utf-8"

                ) as f:

                    self.documents = (
                        json.load(f)
                    )

        except Exception as e:

            print(
                f"FAISS Load Error: {e}"
            )

    # =====================================
    # INFO
    # =====================================

    def info(
        self
    ):

        return {

            "documents":
                len(
                    self.documents
                ),

            "dimension":
                self.dimension,

            "model":
                self.model_name
        }


# ==========================================
# SINGLETON
# ==========================================

vector_store = (
    FAISSVectorStore()
)

