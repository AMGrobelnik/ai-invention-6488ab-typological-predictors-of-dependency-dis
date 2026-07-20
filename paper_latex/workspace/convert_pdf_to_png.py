#!/usr/bin/env python3
"""Convert PDF pages to PNG images at 150 DPI for visual review."""
import fitz  # PyMuPDF
import os

def convert_pdf_to_png(pdf_path, output_dir, dpi=150):
    """Convert each page of PDF to PNG image."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Open PDF
    doc = fitz.open(pdf_path)
    
    # Calculate zoom factor for DPI
    # 72 DPI is the base, so zoom = desired_dpi / 72
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)
    
    page_paths = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Render page to pixmap
        pix = page.get_pixmap(matrix=mat)
        
        # Save as PNG
        output_path = os.path.join(output_dir, f"page_{page_num + 1:02d}.png")
        pix.save(output_path)
        page_paths.append(output_path)
        print(f"Saved {output_path}")
    
    doc.close()
    return page_paths

if __name__ == "__main__":
    pdf_path = "paper.pdf"
    output_dir = "page_images"
    
    print(f"Converting {pdf_path} to PNG images at 150 DPI...")
    page_paths = convert_pdf_to_png(pdf_path, output_dir, dpi=150)
    print(f"\nConverted {len(page_paths)} pages to {output_dir}/")
