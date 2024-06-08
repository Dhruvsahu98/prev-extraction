import os
from pdf2image import convert_from_path

def pdf_to_images(pdf_file, output_folder, dpi=300, fmt="jpg", first_page=1, last_page=None):
    """
    Convert a PDF file to high-quality images and save them to a folder.

    Args:
        pdf_file (str): Path to the PDF file
        output_folder (str): Path to the folder where the images will be saved
        dpi (int): Desired DPI (dots per inch) for the output images (default: 300)
        fmt (str): Output image format (default: "jpeg")
        first_page (int): First page to convert (default: 1)
        last_page (int): Last page to convert (default: None, meaning all pages)
    """
    images = convert_from_path(pdf_file, dpi=dpi, first_page=first_page, last_page=last_page)
    for i, image in enumerate(images):
        image.save(os.path.join(output_folder, f"page_{i+first_page-1}.{fmt}"), fmt, quality=95)

# Example usage:
pdf_file = "C:\\Users\\aksha\\Desktop\\MADII\\IITM\\New\\prev-extraction\\data-extraction\\input\\IIT-M-ENDTERM-AUG-2022---MLP.pdf"
output_folder = "C:\\Users\\aksha\\Desktop\\MADII\\IITM\\New\\prev-yrs-data-bs-ds\\Diploma\\TDS\\Endterm\\AUG-2022\\input"
pdf_to_images(pdf_file, output_folder, dpi=600, fmt="jpeg", first_page=305, last_page=331)  # Convert pages 2-4