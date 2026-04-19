def load_txt(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    return {
        "source": path,
        "content": text
    }