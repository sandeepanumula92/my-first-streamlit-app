import streamlit as st

def display_pdf(file_path):
    # Provide a download button
    with open(file_path, "rb") as file:
        resume_bytes = file.read()
        st.download_button(label="Download Resume", 
                           data=resume_bytes, 
                           file_name="My_Resume.pdf", 
                           mime="application/pdf")

    # Embed PDF directly using HTML
    st.write("### Resume Preview:")
    pdf_display = f"""
    <embed src="data:application/pdf;base64,{resume_bytes.decode('latin1')}" 
           width="700" height="900" type="application/pdf">
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

def main():
    st.title("My Resume Viewer")
    
    if st.button("Show My Resume"):
        display_pdf("your_resume.pdf")

if __name__ == "__main__":
    main()