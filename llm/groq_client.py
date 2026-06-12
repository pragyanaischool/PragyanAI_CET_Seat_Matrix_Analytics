"""
llm/groq_client.py

Groq LLM Client
"""

from groq import Groq

from config.settings import settings

from llm.models import get_model


class GroqClient:

    def __init__(
        self,
        model="smart"
    ):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

        self.model = get_model(
            model
        )

    def generate(
        self,
        prompt,
        temperature=0.2
    ):

        response = (
            self.client.chat.completions.create(
                model=self.model,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=temperature
            )
        )

        return (
            response.choices[0]
            .message.content
        )

    def invoke(
        self,
        prompt
    ):
        return self.generate(
            prompt
        )


groq_llm = GroqClient()
