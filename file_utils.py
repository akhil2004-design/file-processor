import os
import zipfile
import csv
import pdfplumber
from docx import Document
from reportlab.pdfgen import canvas

# Convert DOCX to PDF
def convert_docx_to_pdf(input_file, output_file):
    try:
        doc = Document(input_file)
        c = canvas.Canvas(output_file)
        y = 800
        for para in doc.paragraphs:
            text = para.text.strip()
            if text:
                c.drawString(50, y, text)
                y -= 20
                if y < 50:
                    c.showPage()
                    y = 800
        c.save()
        return f"✅ DOCX converted to PDF"
    except Exception as e:
        return f"❌ Error in DOCX to PDF: {e}"

# Convert DOCX to CSV
def convert_docx_to_csv(input_file, output_file):
    try:
        doc = Document(input_file)
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for para in doc.paragraphs:
                text = para.text.strip()
                if text:
                    writer.writerow([text])
        return f"✅ DOCX converted to CSV"
    except Exception as e:
        return f"❌ Error in DOCX to CSV: {e}"

# Convert CSV to PDF
def convert_csv_to_pdf(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            c = canvas.Canvas(output_file)
            y = 800
            for row in reader:
                line = ', '.join(row)
                c.drawString(50, y, line)
                y -= 20
                if y < 50:
                    c.showPage()
                    y = 800
            c.save()
        return f"✅ CSV converted to PDF"
    except Exception as e:
        return f"❌ Error in CSV to PDF: {e}"

# Convert PDF to CSV
def convert_pdf_to_csv(input_file, output_file):
    try:
        with pdfplumber.open(input_file) as pdf:
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        lines = text.split('\n')
                        for line in lines:
                            writer.writerow([line])
        return f"✅ PDF converted to CSV"
    except Exception as e:
        return f"❌ Error in PDF to CSV: {e}"

# Compress file into zip
def compress_file(input_file, output_file):
    try:
        with zipfile.ZipFile(output_file, 'w') as zipf:
            zipf.write(input_file, os.path.basename(input_file))
        return f"✅ File compressed"
    except Exception as e:
        return f"❌ Error in compression: {e}"
