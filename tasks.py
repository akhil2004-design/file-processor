import os
from file_utils import convert_docx_to_pdf, convert_docx_to_csv, convert_pdf_to_csv, convert_csv_to_pdf, compress_file

def get_file_format(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower().replace(".", "")

def parse_task(task_text):
    task_text = task_text.lower()
    action = ""
    if "convert" in task_text and "pdf" in task_text and "csv" in task_text:
        action = "pdf_to_csv"
    elif "convert" in task_text and "docx" in task_text and "pdf" in task_text:
        action = "docx_to_pdf"
    elif "convert" in task_text and "docx" in task_text and "csv" in task_text:
        action = "docx_to_csv"
    elif "convert" in task_text and "csv" in task_text and "pdf" in task_text:
        action = "csv_to_pdf"
    elif "compress" in task_text:
        action = "compress"
    elif "convert" in task_text and "and compress" in task_text:
        if "docx" in task_text and "pdf" in task_text:
            action = "docx_to_pdf_compress"
        elif "pdf" in task_text and "csv" in task_text:
            action = "pdf_to_csv_compress"
    return action

def execute_task(input_file, task):
    ext = get_file_format(input_file.name)
    output_file = f"files/{input_file.name.split('.')[0]}_converted"
    os.makedirs("files", exist_ok=True)

    if task == "docx_to_pdf":
        output_file += ".pdf"
        return convert_docx_to_pdf(input_file, output_file)
    elif task == "docx_to_csv":
        output_file += ".csv"
        return convert_docx_to_csv(input_file, output_file)
    elif task == "pdf_to_csv":
        output_file += ".csv"
        return convert_pdf_to_csv(input_file, output_file)
    elif task == "csv_to_pdf":
        output_file += ".pdf"
        return convert_csv_to_pdf(input_file, output_file)
    elif task == "compress":
        output_file = f"files/{input_file.name.split('.')[0]}.zip"
        return compress_file(input_file, output_file)
    elif task == "docx_to_pdf_compress":
        pdf_file = f"{output_file}.pdf"
        compress_file(input_file, f"files/{input_file.name.split('.')[0]}.zip")
        convert_docx_to_pdf(input_file, pdf_file)
        compress_file(pdf_file, f"files/{input_file.name.split('.')[0]}_final.zip")
        return f"✅ Docx converted and compressed."
    elif task == "pdf_to_csv_compress":
        csv_file = f"{output_file}.csv"
        convert_pdf_to_csv(input_file, csv_file)
        compress_file(csv_file, f"files/{input_file.name.split('.')[0]}_final.zip")
        return f"✅ PDF converted and compressed."
    else:
        return "❌ Task not supported."

