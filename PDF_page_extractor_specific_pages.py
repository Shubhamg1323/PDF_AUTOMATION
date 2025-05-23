import os
from PyPDF2 import PdfReader, PdfWriter

def extract_specific_pages(folder_path, output_folder, page_numbers):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            try:
                reader = PdfReader(pdf_path)
                total_pages = len(reader.pages)

                writer = PdfWriter()
                extracted_pages = []

                for page_num in page_numbers:
                    index = page_num - 1  # Convert to 0-based index
                    if 0 <= index < total_pages:
                        writer.add_page(reader.pages[index])
                        extracted_pages.append(page_num)

                if extracted_pages:
                    base_name = os.path.splitext(filename)[0]
                    page_list_str = "_".join(str(p) for p in extracted_pages)
                    output_filename = f"{base_name}_pages_{page_list_str}.pdf"
                    output_path = os.path.join(output_folder, output_filename)

                    with open(output_path, "wb") as f_out:
                        writer.write(f_out)

                    print(f"Extracted pages {page_list_str} from: {filename}")
                else:
                    print(f"Skipped {filename} (no matching pages)")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
input_folder = r"C:\Users\shubh\Desktop\test"
output_folder = r"C:\Users\shubh\Desktop\extracted_pages"
pages_to_extract = [2, 4, 6, 7]

extract_specific_pages(input_folder, output_folder, pages_to_extract)
