import pytesseract
from pdf2image import convert_from_path
import os

# --- Configuration ---
PDF_PATH = "pdf/test1.pdf"
OUTPUT_DIR = "output_images"
TEXT_OUTPUT = "output_text.txt"

# Optional: Set path to Tesseract executable (required on Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# --- Step 1: Convert PDF to images ---
print("Converting PDF to images...")
pages = convert_from_path(PDF_PATH, dpi=300)

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- Step 2: Extract text from each image ---
all_text = ""
for i, page in enumerate(pages):
    image_path = os.path.join(OUTPUT_DIR, f"page_{i+1}.png")
    page.save(image_path, "PNG")
    print(f"Processing page {i+1}...")

    # OCR each page image
    text = pytesseract.image_to_string(page, lang="khm+eng") 
    all_text += f"\n\n--- Page {i+1} ---\n{text}"

# --- Step 3: Save text to a file ---
with open(TEXT_OUTPUT, "w", encoding="utf-8") as f:
    f.write(all_text)

print(f"OCR complete! Text saved to: {TEXT_OUTPUT}")

