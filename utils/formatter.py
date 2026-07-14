import re

def sanitize_html(text: str) -> str:
    unsupported_tags = [
        "ul",
        "ol",
        "li",
        "div",
        "span",
        "p",
    ]

    for tag in unsupported_tags:
        text = re.sub(
            rf"</?{tag}[^>]*>",
            "",
            text,
            flags=re.IGNORECASE,
        )

    return text