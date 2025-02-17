import streamlit as st
from PIL import Image
import base64

# Set page config
st.set_page_config(page_title="My Resume", layout="wide")

# Header
st.title("My Professional Resume")
st.write("Click the button below to view my resume")

# Resume content (modify this with your actual resume content)
resume_text = """
Sandeep Anumula
# John Doe

## Education
- **Bachelor of Science in Computer Science**  
  University of Example (2015-2019)

## Experience
- **Software Engineer**  
  Tech Corp (2020-Present)  
  - Developed web applications
  - Managed database systems

## Skills
- Python, JavaScript, SQL
- Machine Learning
- Web Development
"""

# PDF file (replace with your actual PDF path)
pdf_path = "/workspaces/my-first-streamlit-app/your_resume.pdf"

# HTML resume (optional)
html_resume = """
<div style="padding: 15px; border-radius: 5px; background-color: #f0f2f6">
  <h1 style="color: #2e4053">John Doe</h1>
  <h2 style="color: #3498db">Education</h2>
  <ul>
    <li>Bachelor of Science in Computer Science</li>
    <li>University of Example (2015-2019)</li>
  </ul>
</div>
"""

# Display resume on button click
if st.button("📄 View Resume", help="Click to show/hide resume"):
    # Create tabs for different formats
    tab1, tab2, tab3 = st.tabs(["Text Version", "PDF Version", "HTML Version"])
    
    with tab1:
        st.markdown(resume_text)
        
    with tab2:
        try:
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
        except FileNotFoundError:
            st.warning("PDF file not found. Please update the PDF path.")
            
    with tab3:
        st.markdown(html_resume, unsafe_allow_html=True)

# Add download button for PDF
with open(pdf_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📥 Download Resume",
    data=PDFbyte,
    file_name="John_Doe_Resume.pdf",
    mime="application/octet-stream",
)

# Optional: Add profile image
col1, col2 = st.columns([1, 3])
with col1:
    image = Image.open("profile.jpg")  # Add your profile image
    st.image(image, width=200)