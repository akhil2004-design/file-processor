import os

NOTES_DIR = "notes"

def save_note(filename, content):
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)
    path = os.path.join(NOTES_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

def read_note(filename):
    path = os.path.join(NOTES_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return None

