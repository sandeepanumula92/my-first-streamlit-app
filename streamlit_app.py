import streamlit as st
import base64
import os
import tempfile

def display_pdf(file_path):
    # Read the file
    with open(file_path, "rb") as file:
        resume_bytes = file.read()
    
    # Provide a download button
    st.download_button(label="Download Resume", 
                       data=resume_bytes, 
                       file_name="My_Resume.pdf", 
                       mime="application/pdf")
    
    # Create a temporary file to serve the PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(resume_bytes)
        tmp_path = tmp_file.name
    
    # Generate a proper embedded PDF view
    st.write("### Resume Preview:")
    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64.b64encode(resume_bytes).decode()}"
            width="700" height="900" type="application/pdf"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

def main():
    st.title("My Resume Viewer")
    
    if st.button("Show My Resume"):
        display_pdf("your_resume.pdf")

if __name__ == "__main__":
    main()