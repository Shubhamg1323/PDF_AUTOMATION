from PyPDF2 import PdfReader, PdfWriter

def merge_multiple_pdfs(pdf_list, output_path):
    writer = PdfWriter()

    for pdf_path in pdf_list:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f_out:
        writer.write(f_out)

# Example usage
pdfs_to_merge = [
    r"C:\Users\shubh\Desktop\X.pdf",
    r"C:\Users\shubh\Desktop\Y.pdf",
    #r"C:\Users\shubh\Desktop\Z.pdf"  # Add as many as you like
]

merge_multiple_pdfs(pdfs_to_merge, r"C:\Users\shubh\Desktop\Merged_All1.pdf")
