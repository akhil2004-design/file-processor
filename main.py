import streamlit as st
import os
from tasks import get_file_format, execute_tasks

st.title("Smart File Processor")

uploaded_file = st.file_uploader("Upload your file here", type=["pdf", "csv", "docx", "txt"])

if uploaded_file is not None:
    file_details = {
        "filename": uploaded_file.name,
        "filetype": uploaded_file.type,
        "filesize": uploaded_file.size
    }
    st.write(file_details)

    # Save uploaded file temporarily
    os.makedirs("files", exist_ok=True)
    save_path = os.path.join("files", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Detect format from extension
    from_format = get_file_format(save_path)
    st.success(f"Detected format: {from_format}")

    # Select format to convert into
    format_options = ["pdf", "csv", "docx", "txt"]
    format_options = [fmt for fmt in format_options if fmt != from_format]
    to_format = st.selectbox("Select format to convert into", format_options)

    # Compress option
    compress_option = st.checkbox("Also compress the file")

    if st.button("Run Task"):
        actions = ["convert"]
        if compress_option:
            actions.append("compress")

        results, final_file = execute_tasks(save_path, from_format, to_format, actions)

        st.header("Results")
        for res in results:
            st.write(res)

        with open(final_file, "rb") as f:
            data = f.read()
            st.download_button("Download Result", data, file_name=os.path.basename(final_file))
