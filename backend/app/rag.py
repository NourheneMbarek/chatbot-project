from app.loaders.document_loader import load_documents_from_folder
# from app.prompts import build_document_prompt

from app.llm_service import generate_answer

DOCUMENTS: list[dict] = []


def initialize_documents(folder: str = "data") -> None:
    """Load supported documents into memory when the application starts."""

    global DOCUMENTS
    DOCUMENTS = load_documents_from_folder(folder)

    for doc in DOCUMENTS:
        print(f"Loaded: {doc['source']}")
        print(f"Preview: {doc['content'][:200]}")
        print("-----")


def retrieve_documents(question: str, limit: int = 3) -> list[dict]:
    """
    Find the most relevant documents using simple keyword matching.

    This is a lightweight retrieval method and can later be replaced
    with embeddings and vector similarity search.
    """

    normalized_words = {
        word.strip(".,!?;:()[]{}\"'").lower()
        for word in question.split()
        if len(word.strip(".,!?;:()[]{}\"'")) > 2
    }

    matches: list[dict] = []

    for doc in DOCUMENTS:
        content = doc.get("content", "")
        content_lower = content.lower()

        score = sum(
            1 for word in normalized_words
            if word in content_lower
        )

        if score > 0:
            matches.append(
                {
                    "source": doc.get("source", "Unknown source"),
                    "content": content,
                    "score": score,
                }
            )

    matches.sort(key=lambda item: item["score"], reverse=True)

    return matches[:limit]


def search_documents(question: str) -> dict:
    top_matches = retrieve_documents(question)

    if not top_matches:
        return {
            "answer": (
                "I could not find relevant information "
                "in the provided documents."
            ),
            "sources": [],
        }

    context = "\n\n".join(
        (
            f"Source: {match['source']}\n"
            f"Content:\n{match['content'][:1000]}"
        )
        for match in top_matches
    )

    sources = [match["source"] for match in top_matches]

    # prompt = build_document_prompt(
    # question=question,
    # context=context,
    # sources=sources,
    # )

    # answer = generate_answer(prompt)

    answer = generate_answer(
        question=question,
        context=context,
    )


    return {
        "answer": answer,
        "sources": sources,
    }

if __name__ == "__main__":
    initialize_documents("data")

    result = search_documents(
        "What is the vacation policy?"
    )

    print("\nSources:")
    print(result["sources"])

    print("\nGenerated answer:")
    print(result["answer"])