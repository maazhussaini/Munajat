import streamlit as st
import base64

# st.set_page_config(page_title="pdf-GPT", page_icon="📖", layout="wide")
# st.header("pdf-GPT")

def clear_submit():
    st.session_state["submit"] = False


def displayPDF(uploaded_file):
    
    # Read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # Convert to utf-8
    base64_pdf = base64.b64encode(bytes_data).decode('utf-8')

    # Embed PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'

    # Display file
    st.markdown(pdf_display, unsafe_allow_html=True)


with st.sidebar:
    
    uploaded_file = st.file_uploader(
        "Upload file", type=["pdf"], 
        help="Only PDF files are supported", 
        on_change=clear_submit)


col1, col2 = st.columns(spec=[2, 1], gap="small")


if uploaded_file:
    with col1:
        displayPDF(uploaded_file)
    