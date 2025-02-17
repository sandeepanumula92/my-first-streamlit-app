import streamlit as st
import base64

def display_pdf(file_path):
    with open(file_path, "rb") as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def main():
    st.title("My Resume Viewer")
    
    # Button to display the resume
    if st.button("Show My Resume"):
        with open("my_resume.pdf", "rb") as file:
            resume_bytes = file.read()
            st.download_button(label="Download Resume", 
                               data=resume_bytes, 
                               file_name="My_Resume.pdf", 
                               mime="application/pdf")
            st.write("### Resume Preview:")
            display_pdf("my_resume.pdf")

if __name__ == "__main__":
    main()