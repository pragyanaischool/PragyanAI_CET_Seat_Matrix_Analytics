"""
rag/qa_chain.py

Question Answering Chain
"""

from rag.retriever import (
    retriever
)

from llm.groq_client import (
    groq_llm
)

from llm.prompts import (
    CHATBOT_PROMPT
)


class QAChain:

    def __init__(self):

        self.retriever = (
            retriever
        )

        self.llm = (
            groq_llm
        )

    def answer(
        self,
        question
    ):

        context = (
            self.retriever
            .get_context(
                question
            )
        )

        prompt = (
            CHATBOT_PROMPT
            .format(
                context=context,
                question=question
            )
        )

        response = (
            self.llm.generate(
                prompt
            )
        )

        return {

            "question":
                question,

            "context":
                context,

            "answer":
                response
        }


qa_chain = QAChain()
