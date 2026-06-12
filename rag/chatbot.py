"""
rag/chatbot.py

RAG Chatbot Engine
"""

from rag.qa_chain import (
    qa_chain
)


class CollegeChatbot:

    def __init__(self):

        self.qa_chain = (
            qa_chain
        )

        self.chat_history = []

    def ask(
        self,
        query
    ):

        result = (
            self.qa_chain.answer(
                query
            )
        )

        self.chat_history.append({

            "question":
                query,

            "answer":
                result["answer"]
        })

        return result["answer"]

    def history(self):

        return self.chat_history

    def clear(self):

        self.chat_history = []


chatbot = (
    CollegeChatbot()
)
