from openai import OpenAI
from app.prompts import SYSTEM_PROMPT, DOCUMENT_PROMPT
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_answer(question, context):

    prompt = DOCUMENT_PROMPT.format(
        context=context,
        question=question
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=SYSTEM_PROMPT,
        input=prompt,
    )

    return response.output_text