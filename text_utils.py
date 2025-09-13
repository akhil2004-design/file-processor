import re

def clean_text(text):
    # Remove extra whitespace and unwanted chars
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text

def extract_numbers(text):
    # Example: extract all numbers from text
    return re.findall(r"\d+", text)
