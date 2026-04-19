# from pypdf import PdfReader


# def load_pdf(path: str) -> dict:
#     reader = PdfReader(path)
#     pages_text = []

#     for page_number, page in enumerate(reader.pages, start=1):
#         text = page.extract_text() or ""
#         if text.strip():
#             pages_text.append(f"[Page {page_number}]\n{text}")

#     return {
#         "source": path,
#         "content": "\n\n".join(pages_text)
#     }

from pypdf import PdfReader
import re


def clean_pdf_text(text: str) -> str:
    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        line = line.strip()

        # If the line looks like letters separated by spaces, join them
        # Example: "E m p l o y e e  H a n d b o o k"
        if re.fullmatch(r'[\w\s\.\,\-\:]+', line):
            line = re.sub(r'(?<=\b\w) (?=\w\b)', '', line)
            line = re.sub(r'(?<=\w) (?=\w)', '', line)

        line = re.sub(r'\s+', ' ', line).strip()

        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def load_pdf(path: str) -> dict:
    reader = PdfReader(path)
    pages_text = []

    for page_number, page in enumerate(reader.pages, start=1):
        raw_text = page.extract_text() or ""
        cleaned_text = clean_pdf_text(raw_text)

        if cleaned_text.strip():
            pages_text.append(f"[Page {page_number}]\n{cleaned_text}")

    return {
        "source": path,
        "content": "\n\n".join(pages_text)
    }