"""
ui/chatbot_ui.py
"""

import streamlit as st

from rag.chatbot import chatbot


def render_chatbot(df=None):
    """
    AI Counsellor UI
    """

    st.title(
        "🤖 AI CET Counsellor"
    )

    st.markdown(
        """
        Ask questions about:

        - Colleges
        - Branches
        - Districts
        - Seat Matrix
        - Intake Trends
        - AI/ML Colleges
        """
    )

    if "chat_history" not in st.session_state:

        st.session_state[
            "chat_history"
        ] = []

    query = st.chat_input(
        "Ask a question..."
    )

    if query:

        with st.spinner(
            "Thinking..."
        ):

            try:

                response = chatbot.ask(
                    query
                )

            except Exception as e:

                response = (
                    f"Error: {str(e)}"
                )

        st.session_state[
            "chat_history"
        ].append(

            {

                "question":
                    query,

                "answer":
                    response
            }
        )

    for item in reversed(

        st.session_state[
            "chat_history"
        ]

    ):

        with st.chat_message(
            "user"
        ):

            st.write(
                item["question"]
            )

        with st.chat_message(
            "assistant"
        ):

            st.write(
                item["answer"]
            )
            
