from app.loaders.document_loader import load_documents_from_folder


DOCUMENTS = []


def initialize_documents(folder: str = "data"):
    global DOCUMENTS
    DOCUMENTS = load_documents_from_folder(folder)
    for doc in DOCUMENTS:
        print("Loaded:", doc["source"])
        print("Preview:", doc["content"][:200])
        print("-----")


def search_documents(question: str) -> dict:
    q_words = set(question.lower().split())

    best_matches = []

    for doc in DOCUMENTS:
        content = doc["content"]
        content_lower = content.lower()

        score = sum(1 for word in q_words if word in content_lower)

        if score > 0:
            best_matches.append({
                "source": doc["source"],
                "content": content,
                "score": score
            })

    best_matches.sort(key=lambda x: x["score"], reverse=True)

    top_matches = best_matches[:2]

    if not top_matches:
        return {
            "answer": "I could not find relevant information in the provided documents.",
            "sources": []
        }

    combined_text = "\n\n".join(match["content"][:500] for match in top_matches)
    sources = [match["source"] for match in top_matches]

    return {
        "answer": f"Based on the documents, here is the relevant information:\n\n{combined_text}",
        "sources": sources
    }