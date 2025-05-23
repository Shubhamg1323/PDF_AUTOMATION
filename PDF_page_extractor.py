import os
from PyPDF2 import PdfReader, PdfWriter

def extract_page_range(folder_path, output_folder, start_page, end_page):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            try:
                reader = PdfReader(pdf_path)
                total_pages = len(reader.pages)

                # Convert to 0-based index
                start_idx = start_page - 1
                end_idx = end_page

                if total_pages >= start_page:
                    writer = PdfWriter()
                    for i in range(start_idx, min(end_idx, total_pages)):
                        writer.add_page(reader.pages[i])

                    base_name = os.path.splitext(filename)[0]
                    output_filename = f"{base_name}_pages_{start_page}_to_{min(end_page, total_pages)}.pdf"
                    output_path = os.path.join(output_folder, output_filename)

                    with open(output_path, "wb") as f_out:
                        writer.write(f_out)

                    print(f"Extracted pages {start_page}-{min(end_page, total_pages)} from: {filename}")
                else:
                    print(f"Skipped {filename} (has only {total_pages} pages)")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
input_folder = r"C:\Users\shubh\Desktop\test"
output_folder = r"C:\Users\shubh\Desktop\extracted_pages"

# Extract pages 2 through 8
extract_page_range(input_folder, output_folder, start_page=1, end_page=5)
