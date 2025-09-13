import os

ALLOWED_EXTENSIONS = ["pdf", "csv", "docx", "txt"]

def validate_file(uploaded_file):
    _, ext = os.path.splitext(uploaded_file.name)
    ext = ext.lower().replace(".", "")
    if ext not in ALLOWED_EXTENSIONS:
        return False, f"❌ File type {ext} not allowed."
    if uploaded_file.size > 200*1024*1024:
        return False, "❌ File too large (max 200MB)."
    return True, "✅ File is valid."
