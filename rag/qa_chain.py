"""
rag/qa_chain.py

RAG Question Answering Chain
"""

from rag.retriever import (
    retriever
)

from llm.groq_client import (
    groq_llm
)


class QAChain:

    def __init__(self):

        self.retriever = (
            retriever
        )

        self.llm = (
            groq_llm
        )

    # =====================================
    # BUILD PROMPT
    # =====================================

    def build_prompt(
        self,
        question,
        context
    ):

        return f"""
You are an expert Karnataka CET College Counsellor.

Use ONLY the provided context to answer.

If information is not available in the context,
say "Information not found in uploaded seat matrix."

----------------------------------------

CONTEXT:

{context}

----------------------------------------

QUESTION:

{question}

----------------------------------------

ANSWER:
"""

    # =====================================
    # ANSWER QUESTION
    # =====================================

    def answer(
        self,
        question,
        top_k=5
    ):

        context = (
            self.retriever
            .get_context(
                query=question,
                top_k=top_k
            )
        )

        if not context:

            return {

                "question":
                    question,

                "answer":
                    "No relevant information found.",

                "context":
                    ""
            }

        prompt = self.build_prompt(

            question=question,

            context=context
        )

        try:

            response = (
                self.llm.generate(
                    prompt
                )
            )

        except Exception as e:

            response = (
                f"LLM Error: {str(e)}"
            )

        return {

            "question":
                question,

            "answer":
                response,

            "context":
                context
        }

    # =====================================
    # RAW CONTEXT
    # =====================================

    def get_context(
        self,
        query,
        top_k=5
    ):

        return (
            self.retriever
            .get_context(
                query=query,
                top_k=top_k
            )
        )

    # =====================================
    # DEBUG
    # =====================================

    def debug(
        self,
        query
    ):

        docs = (

            self.retriever
            .retrieve_with_scores(
                query
            )

        )

        return {

            "query":
                query,

            "results":
                docs
        }


# ==========================================
# SINGLETON
# ==========================================

qa_chain = QAChain()

