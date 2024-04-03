import streamlit as st
import base64

# Improved caching and function naming, added file path parameter
@st.cache_data()
def encode_pdf_to_base64(pdf_file_path):
    """
    Encodes a PDF file to base64.

    Args:
    pdf_file_path (str): The path to the PDF file.

    Returns:
    str: The base64 encoded string of the PDF file.
    """
    try:
        with open(pdf_file_path, "rb") as pdf_file:
            base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
        return base64_pdf
    except Exception as e:
        st.error(f"Failed to read and encode the PDF file: {e}")
        return None

def main():
    st.title('PDF Viewer App')

    pdf_file_path = "data/Munajat-e-MaqboolByShaykhAshrafAliThanvir.a.pdf"
    pdf_base64 = encode_pdf_to_base64(pdf_file_path)
    
    if pdf_base64:
        pdf_display = f"""
        <div style='height: 80vh; width: 100%;'>
            <iframe src="data:application/pdf;base64,{pdf_base64}" style='height: 100%; width: 100%;' frameborder="0"></iframe>
        </div>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.write("Unable to display the PDF. Please check the console for errors.")

if __name__ == "__main__":
    main()
