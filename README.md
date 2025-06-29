# PDF Automation Scripts

This repository contains a collection of Python scripts for automating common PDF tasks, such as merging and extracting pages.

## Features

- **Bulk PDF Merger**: Merges all PDF files within a specified folder into a single PDF document.
- **Selective PDF Merger**: Merges a user-defined list of PDF files into one.
- **PDF Page Range Extractor**: Extracts a continuous range of pages (e.g., pages 5-10) from every PDF in a given folder.
- **Specific PDF Page Extractor**: Extracts specific, non-contiguous pages (e.g., pages 1, 3, 8) from every PDF in a folder.

## Requirements

This project uses the `PyPDF2` library. You can install it using pip:

```bash
pip install PyPDF2
```

## How to Use

Each script is designed to be run directly. Before running, you must modify the file paths specified within the script to point to your input and output locations.

---

### 1. Bulk PDF Merger (`PDF_bulk_merger.py`)

This script finds all PDF files in a specified input folder, sorts them alphabetically, and merges them into a single output PDF.

**Usage:**

Modify the `input_folder` and `output_file` variables in `PDF_bulk_merger.py`:

```python
# Example usage
input_folder = r"C:\path\to\your\input_folder"
output_file = r"C:\path\to\your\Merged_Output.pdf"

merge_all_pdfs_in_folder(input_folder, output_file)
```

---

### 2. Selective PDF Merger (`PDF_merger.py`)

This script merges a specific list of PDF files into a single output file.

**Usage:**

Update the `pdfs_to_merge` list and the output path in `PDF_merger.py`:

```python
# Example usage
pdfs_to_merge = [
    r"C:\path\to\your\first.pdf",
    r"C:\path\to\your\second.pdf",
    r"C:\path\to\your\third.pdf"
]
output_path = r"C:\path\to\your\Merged_Selective.pdf"

merge_multiple_pdfs(pdfs_to_merge, output_path)
```

---

### 3. PDF Page Range Extractor (`PDF_page_extractor.py`)

This script processes every PDF in an input folder and extracts a specified range of pages from each, saving them as new PDF files in an output folder.

**Usage:**

Set the `input_folder`, `output_folder`, `start_page`, and `end_page` variables in `PDF_page_extractor.py`:

```python
# Example usage
input_folder = r"C:\path\to\your\input_folder"
output_folder = r"C:\path\to\your\output_folder"

# Extract pages 1 through 2 from each PDF
extract_page_range(input_folder, output_folder, start_page=1, end_page=2)
```

---

### 4. Specific PDF Page Extractor (`PDF_page_extractor_specific_pages.py`)

This script processes every PDF in an input folder and extracts a list of specific page numbers from each.

**Usage:**

Define the `input_folder`, `output_folder`, and the `pages_to_extract` list in `PDF_page_extractor_specific_pages.py`:

```python
# Example usage
input_folder = r"C:\path\to\your\input_folder"
output_folder = r"C:\path\to\your\output_folder"

# Extracts pages 1, 2, and 3 from each PDF
pages_to_extract = [1, 2, 3]  # or list(range(1, 4))

extract_specific_pages(input_folder, output_folder, pages_to_extract)
```