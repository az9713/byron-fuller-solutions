import argparse
from pypdf import PdfReader, PdfWriter

def extract_pages(input_path, start_page, end_page, output_path="extracted_pages.pdf"):
    """
    Extracts a specific range of pages from a PDF.
    Note: Page numbering in this script starts at 1.
    """
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    # Validate page range
    total_pages = len(reader.pages)
    if start_page < 1 or end_page > total_pages or start_page > end_page:
        print(f"Error: Invalid range {start_page}-{end_page}. Total pages: {total_pages}")
        return

    # Extract pages (converting 1-based user input to 0-based indexing)
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])
    
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"Successfully saved pages {start_page} to {end_page} in '{output_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a PDF by page range.")
    parser.add_argument("filename", help="The name/path of the PDF file to split.")
    parser.add_argument("start", type=int, help="The starting page number (inclusive, 1-indexed).")
    parser.add_argument("end", type=int, help="The ending page number (inclusive, 1-indexed).")
    parser.add_argument("-o", "--output", default="extracted.pdf", help="Output filename (default: extracted.pdf).")
    
    args = parser.parse_args()
    extract_pages(args.filename, args.start, args.end, args.output)
