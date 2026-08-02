import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def generate_answer(prompt: str) -> str:
    """Send a complete prompt to the LLM."""

    try:
        response = client.responses.create(
            model=MODEL,
            input=prompt,
        )

        return response.output_text.strip()

    except Exception as e:
        print(f"OpenAI Error: {e}")
        return "Sorry, I couldn't generate an answer."