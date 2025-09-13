import os
from file_utils import convert_docx_to_pdf, convert_docx_to_csv, convert_csv_to_pdf, convert_pdf_to_csv, compress_file

def get_file_format(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower().replace(".", "")

def parse_task(text):
    text = text.lower()
    formats = ["pdf", "csv", "docx", "txt"]
    from_format = None
    to_format = None
    actions = []

    if "convert" in text or "change" in text or "बदल" in text:
        actions.append("convert")
    if "compress" in text or "zip" in text:
        actions.append("compress")

    mentioned_formats = []
    for fmt in formats:
        if fmt in text:
            mentioned_formats.append(fmt)

    if len(mentioned_formats) >= 2:
        from_format = mentioned_formats[0]
        to_format = mentioned_formats[1]
    elif len(mentioned_formats) == 1:
        from_format = mentioned_formats[0]

    for fmt in formats:
        if f"into {fmt}" in text or f"to {fmt}" in text or f"in {fmt}" in text:
            to_format = fmt

    if to_format == "doc":
        to_format = "docx"
    if from_format == "doc":
        from_format = "docx"

    return from_format, to_format, actions

def execute_tasks(file_path, from_format, to_format, actions):
    results = []
    current_file = file_path
    base, ext = os.path.splitext(file_path)

    if "convert" in actions and from_format and to_format:
        output_file = f"{base}_converted.{to_format}"
        if from_format == "docx" and to_format == "pdf":
            results.append(convert_docx_to_pdf(current_file, output_file))
        elif from_format == "docx" and to_format == "csv":
            results.append(convert_docx_to_csv(current_file, output_file))
        elif from_format == "csv" and to_format == "pdf":
            results.append(convert_csv_to_pdf(current_file, output_file))
        elif from_format == "pdf" and to_format == "csv":
            results.append(convert_pdf_to_csv(current_file, output_file))
        else:
            results.append(f"❌ Conversion from {from_format} to {to_format} not supported yet.")
        current_file = output_file

    if "compress" in actions:
        zip_file = f"{base}_compressed.zip"
        results.append(compress_file(current_file, zip_file))
        current_file = zip_file

    return results, current_file
