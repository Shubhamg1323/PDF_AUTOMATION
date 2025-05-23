import os
from PyPDF2 import PdfReader, PdfWriter

def merge_all_pdfs_in_folder(folder_path, output_path):
    writer = PdfWriter()

    # Get a sorted list of all PDF files
    pdf_files = sorted([
        f for f in os.listdir(folder_path) 
        if f.lower().endswith(".pdf")
    ])

    for pdf_file in pdf_files:
        full_path = os.path.join(folder_path, pdf_file)
        try:
            reader = PdfReader(full_path)
            for page in reader.pages:
                writer.add_page(page)
            print(f"Added: {pdf_file}")
        except Exception as e:
            print(f"Failed to read {pdf_file}: {e}")

    # Save the merged output
    with open(output_path, "wb") as f_out:
        writer.write(f_out)
    print(f"\n✅ Merged PDF saved as: {output_path}")

# Example usage
input_folder = r"C:\Users\shubh\Desktop\test1"
output_file = r"C:\Users\shubh\Desktop\Merged_All_Test1.pdf"

merge_all_pdfs_in_folder(input_folder, output_file)
