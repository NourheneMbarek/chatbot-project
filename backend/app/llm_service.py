import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from app.prompts import DOCUMENT_PROMPT

load_dotenv()

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

llm = ChatOpenAI(
    model=MODEL,
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0,
)

output_parser = StrOutputParser()

document_chain = DOCUMENT_PROMPT | llm | output_parser


def generate_answer(
    question: str,
    context: str,
) -> str:
    """Generate a grounded answer using LangChain."""

    try:
        return document_chain.invoke(
            {
                "question": question,
                "context": context,
            }
        ).strip()

    except Exception as e:
        print(f"LangChain / OpenAI Error: {e}")

        return "Sorry, I couldn't generate an answer."

# import os

# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )

# MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


# def generate_answer(prompt: str) -> str:
#     """Send a complete prompt to the LLM."""

#     try:
#         response = client.responses.create(
#             model=MODEL,
#             input=prompt,
#         )

#         return response.output_text.strip()

#     except Exception as e:
#         print(f"OpenAI Error: {e}")
#         return "Sorry, I couldn't generate an answer."