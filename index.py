import streamlit as st
import fitz  # PyMuPDF
import io


st.set_page_config(page_title="Munajat-e-Maqbool", page_icon="data/favicon.ico", layout="centered")

def Munajaat(zoom, page_title):
    
    st.title("Munajat-e-Maqbool")
    # Using a wide page layout

    # Path to PDF file
    pdf_file_path = "data/Munajat-e-MaqboolByShaykhAshrafAliThanvir.a.pdf"

    # Provide a download button for the entire PDF file
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(label="Download PDF",
                            data=pdf_bytes,
                            file_name=f"{page_title}.pdf",
                            mime="application/pdf")
    
    if pdf_file_path:
        # Open the PDF file directly from the file path
        pdf_document = fitz.open(pdf_file_path)

        # Use a container to control layout
        with st.container():
            # Create three columns
            left_spacer, content, right_spacer = st.columns([1,3,1])  # Adjust the ratio as needed

            with content:  # This ensures content is in the middle column
                # Display each page of the PDF as an image
                for page_num in range(pdf_document.page_count):
                    page = pdf_document.load_page(page_num)  # Load the page
                    # Define zoom factor: 5x zoom
                    # zoom = 3
                    mat = fitz.Matrix(zoom, zoom)  # Zoom factor for both x and y axes
                    
                    pix = page.get_pixmap(matrix=mat)  # Render page to an image with zoom
                    image_stream = io.BytesIO(pix.tobytes("png"))  # Get image bytes
                    # st.image(image_stream, caption=f"Page {page_num + 1}", use_container_width=True)
                    st.image(image_stream, caption=f"Page {page_num + 1}", output_format = "auto")  # Adjust width as needed


def Zariat(zoom, page_title):
    st.title(page_title)
    # Using a wide page layout

    # Path to PDF file
    pdf_file_path = "data/Zariatul-Wusool.pdf"

    # Provide a download button for the entire PDF file
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(label="Download PDF",
                            data=pdf_bytes,
                            file_name=f"{page_title}.pdf",
                            mime="application/pdf")
    
    if pdf_file_path:
        # Open the PDF file directly from the file path
        pdf_document = fitz.open(pdf_file_path)

        # Use a container to control layout
        with st.container():
            # Create three columns
            left_spacer, content, right_spacer = st.columns([1,3,1])  # Adjust the ratio as needed

            with content:  # This ensures content is in the middle column
                # Display each page of the PDF as an image
                for page_num in range(pdf_document.page_count):
                    page = pdf_document.load_page(page_num)  # Load the page
                    # Define zoom factor: 5x zoom
                    # zoom = 3
                    mat = fitz.Matrix(zoom, zoom)  # Zoom factor for both x and y axes
                    
                    pix = page.get_pixmap(matrix=mat)  # Render page to an image with zoom
                    image_stream = io.BytesIO(pix.tobytes("png"))  # Get image bytes
                    # st.image(image_stream, caption=f"Page {page_num + 1}", use_container_width=True)
                    st.image(image_stream, caption=f"Page {page_num + 1}", output_format = "auto")  # Adjust width as needed



def main():
    # Using object notation
    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Munajat-e-Maqbool", "Zariatul-Wusool")
    )

    zoom = st.sidebar.slider('Zoom', 1.75, 4.5)

    if add_selectbox == "Munajat-e-Maqbool":
        Munajaat(zoom, add_selectbox)
    else:
        Zariat(zoom, add_selectbox)
    
if __name__ == "__main__":
    main()