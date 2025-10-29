# Khmer OCR (Tesseract) — khmerOCR_Tesseract

Small collection of example scripts that demonstrate using Tesseract OCR from Python to extract text from images and PDFs. The scripts are simple examples and write output text files to the repository.

## Contents

- `image2text.py` — Example that opens an image (`images/test1.jpg`), runs Tesseract OCR (English + Khmer), and writes the result to `output2.txt`.
- `pdf2text.py` — Converts `pdf/wadding.pdf` into images (`output_images/`), runs OCR on each page (English by default), and writes the combined text to `output_text.txt`.
- `images/` — place image files here for `image2text.py`.
- `pdf/` — place PDF files here for `pdf2text.py`.
- `outputt/` and other `output_*.txt` files contain example outputs.

## Prerequisites

- Python 3.8 or newer.
- Tesseract OCR installed on your system.
  - Windows default installer installs Tesseract to `C:\Program Files\Tesseract-OCR\tesseract.exe`.
  - Make sure Khmer language data (`khm.traineddata`) is installed in Tesseract's `tessdata` folder if you need Khmer OCR.
  - Tesseract download: https://github.com/tesseract-ocr/tesseract
## Python packages

Install the required Python libraries (PowerShell):

```powershell
pip install pytesseract pillow pdf2image
```

If you prefer a `requirements.txt`, create one with:

```
pytesseract
Pillow
pdf2image
```

## Configure Tesseract path (Windows)

Both example scripts set the Tesseract executable path inside the script. If your Tesseract is installed in a different location, update the path in the scripts:

- `image2text.py` sets
  `pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`
- `pdf2text.py` sets
  `pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"`

Or, remove those lines if `tesseract` is available on your system PATH.

## Usage examples (PowerShell)

1) OCR a single image (uses `images/test1.jpg` by default in `image2text.py`):

```powershell
python image2text.py
# Output: text printed to console and saved to `output2.txt`
```

2) OCR a PDF (uses `pdf/wadding.pdf` by default in `pdf2text.py`):

```powershell
python pdf2text.py
# Output: intermediate images saved in `output_images/` and combined text in `output_text.txt`
```

Note: The scripts are simple examples — they do not accept command-line arguments. To OCR different files, edit the `PDF_PATH`, image path, or output filenames directly inside the scripts.

## Tips & Notes

- To enable Khmer OCR, ensure you have the `khm.traineddata` file in Tesseract's `tessdata` folder. You can then change the language parameter in the scripts:
  - Example for images: `pytesseract.image_to_string(img, lang='eng+khm')`
  - Example for PDF pages: `pytesseract.image_to_string(page, lang='khm')`
- For better results, experiment with Tesseract configs such as `--oem` and `--psm` (see Tesseract docs).
- If `pdf2image.convert_from_path` fails, verify Poppler is installed and its `bin` directory is on PATH. You can also pass `poppler_path` to `convert_from_path`.

## Troubleshooting

- If you see an error locating `tesseract.exe`, update `pytesseract.pytesseract.tesseract_cmd` or add Tesseract to PATH.
- If PDF conversion fails, ensure Poppler is installed and accessible.
- If Khmer text is garbled, confirm `khm.traineddata` is installed and try increasing DPI when converting PDF pages (e.g., `dpi=300`).

## Contact

If you need help or want to connect, email: phon.sobon02@gmail.com

---

If you'd like, I can:

- make the scripts accept command-line arguments for input and output files,
- add a `requirements.txt`, or
- add a small example image and a sample PDF to the repo.

Tell me which of those you'd like next.
