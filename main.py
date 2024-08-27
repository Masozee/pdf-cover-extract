import os
import shutil
from pdf2image import convert_from_path
from PIL import Image
from tqdm import tqdm

def extract_cover(pdf_path, output_folder, extracted_folder, pbar):
    try:
        # Convert only the first page of the PDF to an image
        pages = convert_from_path(pdf_path, first_page=1, last_page=1)
        
        if pages:
            # Get the first page
            cover = pages[0]
            
            # Save as PNG with the same name as the PDF
            output_filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".png"
            output_path = os.path.join(output_folder, output_filename)
            cover.save(output_path, "PNG")
            
            # Move the processed PDF to the extracted folder
            shutil.move(pdf_path, os.path.join(extracted_folder, os.path.basename(pdf_path)))
            
            pbar.set_postfix({"status": f"Saved {output_filename} and moved PDF"})
        else:
            pbar.set_postfix({"status": f"No pages found in {os.path.basename(pdf_path)}"})
    except Exception as e:
        pbar.set_postfix({"status": f"Error: {str(e)}"})
    finally:
        pbar.update(1)

def process_folder(input_folder, output_folder, extracted_folder):
    # Create output and extracted folders if they don't exist
    for folder in [output_folder, extracted_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    # Get list of PDF files
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
    
    # Process all PDFs in the input folder with progress bar
    with tqdm(total=len(pdf_files), desc="Processing PDFs", unit="file") as pbar:
        for filename in pdf_files:
            pdf_path = os.path.join(input_folder, filename)
            extract_cover(pdf_path, output_folder, extracted_folder, pbar)

# Usage
input_folder = 'data'  # Folder containing PDFs
output_folder = 'covers'  # Folder to save extracted covers
extracted_folder = 'extracted'  # Folder to move processed PDFs
process_folder(input_folder, output_folder, extracted_folder)