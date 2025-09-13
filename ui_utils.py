# ui_utils.py

from simlite import Environment
from file_utils import convert_doc_to_pdf, compress_file

def run_ui():
    env = Environment()

    def on_convert():
        input_file = env.input("Enter path of .docx file:")
        output_file = input_file.replace(".docx", ".pdf")
        result = convert_doc_to_pdf(input_file, output_file)
        env.alert(result)

    def on_compress():
        input_file = env.input("Enter path of file to compress:")
        output_file = input_file + ".zip"
        result = compress_file(input_file, output_file)
        env.alert(result)

    env.window("File Processor")
    env.button("Convert DOCX to PDF", on_convert)
    env.button("Compress File", on_compress)
    env.run()
