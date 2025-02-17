import streamlit as st

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
            pdf_display = f'<iframe src="my_resume.pdf" width="700" height="900"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

if __name__ == "__main__":
    main()