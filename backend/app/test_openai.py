import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY was not found. Check the backend/.env file."
    )

client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model=model,
        instructions=(
            "You are a helpful assistant. "
            "Answer clearly and in one sentence."
        ),
        input="What is FastAPI?",
    )

    print("API test successful!")
    print("Model:", model)
    print("Answer:", response.output_text)

except Exception as error:
    print("API test failed.")
    print(type(error).__name__)
    print(error)