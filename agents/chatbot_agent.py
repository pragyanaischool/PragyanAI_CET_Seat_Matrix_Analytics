"""
agents/chatbot_agent.py
"""

from rag.chatbot import (
    chatbot
)


class ChatbotAgent:

    def __init__(self):

        self.chatbot = chatbot

    def run(
        self,
        query
    ):

        return self.chatbot.ask(
            query
        )
