import re

def clean_text(text):
    # Remove multiple spaces, newlines, etc.
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
