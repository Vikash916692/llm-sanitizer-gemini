import re
import bleach

def sanitize_input(user_input):
    clean = bleach.clean(user_input, tags=[], strip=True)

    patterns = [
        r"(?i)ignore previous instructions",
        r"(?i)pretend to be",
        r"(?i)disregard safety",
        r"(?i)you are now",
    ]
    for pattern in patterns:
        clean = re.sub(pattern, "[REDACTED]", clean)
    return clean

def sanitize_output(response_text):
    patterns = [
        r"\b\d{16}\b",  # Credit card numbers
        r"\b\d{3}-\d{2}-\d{4}\b",  # SSNs
        r"(?i)\bpassword\b.*",
        r"(?i)offensive_term",
    ]
    for pattern in patterns:
        response_text = re.sub(pattern, "[SENSITIVE]", response_text)
    return response_text
