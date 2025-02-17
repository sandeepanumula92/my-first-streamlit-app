import streamlit as st
import os
import tempfile

def display_pdf(file_path):
    with open(file_path, "rb") as file:
        resume_bytes = file.read()
        st.download_button(label="Download Resume", 
                           data=resume_bytes, 
                           file_name="My_Resume.pdf", 
                           mime="application/pdf")
    
    # Create a temporary file to serve the PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(resume_bytes)
        tmp_path = tmp_file.name
    
    # Display the PDF using an iframe
    pdf_display = f'<iframe src="file://{tmp_path}" width="700" height="900"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def main():
    st.title("My Resume Viewer")
    
    if st.button("Show My Resume"):
        display_pdf("your_resume.pdf")

if __name__ == "__main__":
    main()