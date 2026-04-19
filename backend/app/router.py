def detect_intent(question: str) -> str:
    q = question.lower()

    dynamic_keywords = [
        "how many vacation days do i have left",
        "how many days do i have left",
        "remaining vacation days",
        "vacation balance",
        "my vacation days",
        "days left for me",
        "how many holidays do i have left"
    ]

    if any(keyword in q for keyword in dynamic_keywords):
        return "TOOL_VACATION"

    return "DOCUMENT_SEARCH"