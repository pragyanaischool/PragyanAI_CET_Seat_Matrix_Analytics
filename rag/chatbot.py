"""
rag/chatbot.py

CET College Intelligence Chatbot
Uses:
    - FAISS Retriever
    - QA Chain
    - Groq LLM

Compatible with:
    ui/chatbot_ui.py
"""

from rag.qa_chain import (
    qa_chain
)


class CollegeChatbot:

    def __init__(self):

        self.qa_chain = qa_chain

        self.chat_history = []

    # =====================================
    # ASK QUESTION
    # =====================================

    def ask(
        self,
        query
    ):

        try:

            result = (
                self.qa_chain.answer(
                    question=query
                )
            )

            answer = result.get(
                "answer",
                "No answer generated."
            )

            self.chat_history.append(

                {

                    "question":
                        query,

                    "answer":
                        answer
                }

            )

            return answer

        except Exception as e:

            error_msg = (
                f"Chatbot Error: {str(e)}"
            )

            self.chat_history.append(

                {

                    "question":
                        query,

                    "answer":
                        error_msg
                }

            )

            return error_msg

    # =====================================
    # ASK WITH DETAILS
    # =====================================

    def ask_detailed(
        self,
        query
    ):

        try:

            result = (
                self.qa_chain.answer(
                    question=query
                )
            )

            self.chat_history.append(

                {

                    "question":
                        query,

                    "answer":
                        result.get(
                            "answer",
                            ""
                        )
                }

            )

            return result

        except Exception as e:

            return {

                "question":
                    query,

                "answer":
                    f"Error: {str(e)}",

                "context":
                    ""
            }

    # =====================================
    # CHAT HISTORY
    # =====================================

    def get_history(
        self
    ):

        return self.chat_history

    # =====================================
    # CLEAR CHAT
    # =====================================

    def clear_history(
        self
    ):

        self.chat_history = []

    # =====================================
    # LAST N CHATS
    # =====================================

    def recent_history(
        self,
        n=10
    ):

        return self.chat_history[-n:]

    # =====================================
    # CHAT COUNT
    # =====================================

    def total_questions(
        self
    ):

        return len(
            self.chat_history
        )

    # =====================================
    # HEALTH CHECK
    # =====================================

    def health(
        self
    ):

        try:

            return {

                "status":
                    "healthy",

                "chat_history":
                    len(
                        self.chat_history
                    )
            }

        except Exception as e:

            return {

                "status":
                    "error",

                "message":
                    str(e)
            }


# ==========================================
# SINGLETON INSTANCE
# ==========================================

chatbot = CollegeChatbot()

