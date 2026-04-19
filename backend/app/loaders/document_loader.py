import os
from app.loaders.txt_loader import load_txt
from app.loaders.md_loader import load_md
from app.loaders.pdf_loader import load_pdf


def load_document(path: str) -> dict:
    if path.endswith(".txt"):
        return load_txt(path)
    if path.endswith(".md"):
        return load_md(path)
    if path.endswith(".pdf"):
        return load_pdf(path)

    raise ValueError(f"Unsupported file type: {path}")


def load_documents_from_folder(folder: str) -> list[dict]:
    documents = []

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        if not os.path.isfile(path):
            continue

        try:
            doc = load_document(path)
            documents.append(doc)
        except ValueError:
            continue

    return documents