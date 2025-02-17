import streamlit as st
import base64

def get_pdf_download_link(pdf_path):
    """Creates a link to download the PDF file"""
    with open(pdf_path, "rb") as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")
    
    pdf_display = f"""
    <embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf">
    """
    return pdf_display

def main():
    st.title("My Resume Viewer")
    
    pdf_path = "your_resume.pdf"  # Ensure this file exists in the same directory

    if st.button("Show My Resume"):
        # Provide a Download Button
        with open(pdf_path, "rb") as pdf_file:
            resume_bytes = pdf_file.read()
            st.download_button(label="Download Resume", 
                               data=resume_bytes, 
                               file_name="My_Resume.pdf", 
                               mime="application/pdf")

        # Display PDF preview
        st.markdown(get_pdf_download_link(pdf_path), unsafe_allow_html=True)

if __name__ == "__main__":
    main()