# main.py
import streamlit as st
import os
from file_utils import *

# Create folder to store uploaded and output files
UPLOAD_DIR = "files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("Smart File Processor")

uploaded_file = st.file_uploader(
    "Upload your file here",
    type=["pdf", "csv", "docx", "txt"]
)

if uploaded_file:
    st.success(f"✅ File is valid: {uploaded_file.name}")
    
    # Save uploaded file to local folder
    input_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Dropdown options for tasks
    operation = st.selectbox(
        "Select the operation you want to perform",
        [
            "Convert DOCX → PDF",
            "Convert DOCX → CSV",
            "Convert PDF → TXT",
            "Convert PDF → CSV",
            "Convert CSV → DOCX",
            "Convert CSV → PDF",
            "Convert TXT → DOCX",
            "Convert TXT → PDF",
            "Compress File",
            "Convert DOCX → PDF and Compress",
            "Convert PDF → CSV and Compress"
        ]
    )
    
    output_file = None
    result_msg = ""
    
    if st.button("Execute Task"):
        filename, ext = os.path.splitext(uploaded_file.name)
        
        try:
            # Single conversion tasks
            if operation == "Convert DOCX → PDF":
                output_file = os.path.join(UPLOAD_DIR, f"{filename}.pdf")
                result_msg = convert_docx_to_pdf(input_path, output_file)
            
            elif operation == "Convert DOCX → CSV":
                output_file = os.path.join(UPLOAD_DIR, f"{filename}.csv")
                result_msg = convert_docx_to_csv(input_path, output_file)
            
            elif operation == "Convert PDF → TXT":
                output_file = os.path.join(UPLOAD_DIR, f"{filename}.txt")
                result_msg = convert_pdf_to_txt(input_path, output_file)
            
            elif operation == "Convert PDF → CSV":
                output_file = os.path.join(UPLOAD_DIR, f"{filename}.csv")
                result_msg = convert_pdf_to_csv(input_path, output_file)
            
            elif operation == "Convert CSV → DOCX":
                output_file = os.path.join(UPLOAD_DIR, f"{filename}.docx")
                result_msg = convert_csv_to_docx(input_path, output_file)
            
            elif operation == "Convert CSV → PDF":
                output_file = os.path.join(UPLOAD_DIR, f"{filename}.pdf")
                result_msg = convert_csv_to_pdf(input_path, output_file)
            
            elif operation == "Convert TXT → DOCX":
                output_file = os.path.join(UPLOAD_DIR, f"{filename}.docx")
                result_msg = convert_txt_to_docx(input_path, output_file)
            
            elif operation == "Convert TXT → PDF":
                output_file = os.path.join(UPLOAD_DIR, f"{filename}.pdf")
                result_msg = convert_txt_to_pdf(input_path, output_file)
            
            # Compression only
            elif operation == "Compress File":
                output_file = os.path.join(UPLOAD_DIR, f"{filename}_compressed.zip")
                result_msg = compress_file(input_path, output_file)
            
            # Combo tasks
            elif operation == "Convert DOCX → PDF and Compress":
                temp_file = os.path.join(UPLOAD_DIR, f"{filename}.pdf")
                msg1 = convert_docx_to_pdf(input_path, temp_file)
                output_file = os.path.join(UPLOAD_DIR, f"{filename}_pdf_compressed.zip")
                msg2 = compress_file(temp_file, output_file)
                result_msg = f"{msg1}\n{msg2}"
            
            elif operation == "Convert PDF → CSV and Compress":
                temp_file = os.path.join(UPLOAD_DIR, f"{filename}.csv")
                msg1 = convert_pdf_to_csv(input_path, temp_file)
                output_file = os.path.join(UPLOAD_DIR, f"{filename}_csv_compressed.zip")
                msg2 = compress_file(temp_file, output_file)
                result_msg = f"{msg1}\n{msg2}"
            
            # Show result message
            st.text(result_msg)
            
            # Provide download button if output file exists
            if output_file and os.path.exists(output_file):
                with open(output_file, "rb") as f:
                    st.download_button(
                        label="Download Output File",
                        data=f,
                        file_name=os.path.basename(output_file)
                    )
        except Exception as e:
            st.error(f"❌ Task failed: {e}")
