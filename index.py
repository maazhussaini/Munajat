import streamlit as st
import fitz  # PyMuPDF
import io


st.set_page_config(page_title="Munajat-e-Maqbool", page_icon="data/favicon.ico", layout="wide")

def Munajaat():
    
    # Path to PDF file
    pdf_file_path = "data/Munajat-e-MaqboolByShaykhAshrafAliThanvir.a.pdf"
    
    with st.container():
        
        col1, col2, col3, col4 = st.columns([1, 5, 2, 1])
        
        with col3:
            # Provide a download button for the entire PDF file
            with open(pdf_file_path, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
                st.download_button(label="Download PDF",
                                data=pdf_bytes,
                                file_name=f"Munajat-e-Maqbool.pdf",
                                mime="application/pdf",
                                use_container_width=True)
                
            
        
        with col2:
            st.header("Munajat-e-Maqbool")
        
        left, center, right = st.columns([1, 7, 1])  
        with center:
            st.divider()
    
    if pdf_file_path:
        # Open the PDF file directly from the file path
        pdf_document = fitz.open(pdf_file_path)

        # Use a container to control layout
        with st.container():
            # Create three columns
            left_spacer, content, right_spacer = st.columns([1,3,1])  # Adjust the ratio as needed

            with content:  # This ensures content is in the middle column
                
                # Initialize the progress bar
                progress_bar = st.progress(0)
                
                # Display each page of the PDF as an image
                for page_num in range(pdf_document.page_count):
                    
                    # Update the progress bar
                    progress_bar.progress((page_num + 1) / pdf_document.page_count)
                    
                    page = pdf_document.load_page(page_num)  # Load the page
                    
                    # Define zoom factor: 1.75x zoom
                    zoom = 1.75
                    mat = fitz.Matrix(zoom, zoom)  # Zoom factor for both x and y axes
                    
                    pix = page.get_pixmap(matrix=mat)  # Render page to an image with zoom
                    image_stream = io.BytesIO(pix.tobytes("png"))  # Get image bytes
                    # st.image(image_stream, caption=f"Page {page_num + 1}", use_container_width=True)
                    st.image(image_stream, caption=f"Page {page_num + 1}", output_format = "auto")  # Adjust width as needed

                progress_bar.empty()

def Zariat():
    # Path to PDF file
    pdf_file_path = "data/Zariatul-Wusool.pdf"

    with st.container():
        
        col1, col2, col3, col4 = st.columns([1, 5, 2, 1])
        
        with col3:
            # Provide a download button for the entire PDF file
            with open(pdf_file_path, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
                st.download_button(label="Download PDF",
                                    data=pdf_bytes,
                                    file_name=f"Zariatul-Wusool.pdf",
                                    mime="application/pdf")
                
            
        
        with col2:
            st.header("Zariatul-Wusool")
        
        left, center, right = st.columns([1, 7, 1])  
        with center:
            st.divider()
    
    if pdf_file_path:
        # Open the PDF file directly from the file path
        pdf_document = fitz.open(pdf_file_path)

        # Use a container to control layout
        with st.container():
            # Create three columns
            left_spacer, content, right_spacer = st.columns([1,3,1])  # Adjust the ratio as needed

            with content:  # This ensures content is in the middle column
                
                # Initialize the progress bar
                progress_bar = st.progress(0)
                
                # Display each page of the PDF as an image
                for page_num in range(pdf_document.page_count):
                    
                    # Update the progress bar
                    progress_bar.progress((page_num + 1) / pdf_document.page_count)
                    
                    page = pdf_document.load_page(page_num)  # Load the page
                    
                    # Define zoom factor: 1.75x zoom
                    zoom = 1.75
                    mat = fitz.Matrix(zoom, zoom)  # Zoom factor for both x and y axes
                    
                    pix = page.get_pixmap(matrix=mat)  # Render page to an image with zoom
                    image_stream = io.BytesIO(pix.tobytes("png"))  # Get image bytes
                    # st.image(image_stream, caption=f"Page {page_num + 1}", use_container_width=True)
                    st.image(image_stream, caption=f"Page {page_num + 1}", output_format = "auto")  # Adjust width as needed

                progress_bar.empty()


def main():
    # Using object notation
    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Munajat-e-Maqbool", "Zariatul-Wusool")
    )

    if add_selectbox == "Munajat-e-Maqbool":
        Munajaat()
    else:
        Zariat()
    
if __name__ == "__main__":
    main()