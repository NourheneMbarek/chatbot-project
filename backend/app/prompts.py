SYSTEM_PROMPT = """
You are an internal HR assistant.

Follow these rules:
- Answer only from the provided document context.
- Do not invent information.
- If the answer is not present, say that you could not find it.
- Keep the answer clear and concise.
- Mention the source documents when useful.
""".strip()


DOCUMENT_PROMPT_TEMPLATE = """
{system_prompt}

Document context:
{context}

User question:
{question}

Sources:
{sources}

Answer:
""".strip()


def build_document_prompt(
    question: str,
    context: str,
    sources: list[str],
) -> str:
    """Build a reusable prompt from retrieved document context."""

    source_text = ", ".join(sources) if sources else "No sources found"

    return DOCUMENT_PROMPT_TEMPLATE.format(
        system_prompt=SYSTEM_PROMPT,
        context=context,
        question=question,
        sources=source_text,
    )