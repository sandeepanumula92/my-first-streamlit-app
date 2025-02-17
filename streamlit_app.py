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
            st.pdf("your_resume.pdf")

if __name__ == "__main__":
    main()