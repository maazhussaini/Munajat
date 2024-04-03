import streamlit as st
import base64

def main():
    st.title('PDF Viewer App')

    # Path to PDF file
    pdf_file_path = "data/Munajat-e-MaqboolByShaykhAshrafAliThanvir.a.pdf"

    # Function to get Base64 encoded string of PDF file
    def get_pdf_file_as_base64(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
        return base64_pdf

    # Embedding PDF in the app with a more adaptive view
    pdf_base64 = get_pdf_file_as_base64(pdf_file_path)
    pdf_display = f"""
    <div style='height: 80vh; width: 100%;'>
        <iframe src="data:application/pdf;base64,{pdf_base64}" style='height: 100%; width: 100%;' frameborder="0"></iframe>
    </div>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
