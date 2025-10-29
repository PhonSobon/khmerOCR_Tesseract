# Khmer OCR (Tesseract) — khmerOCR_Tesseract

A web application with Flask API and modern UI for extracting text from images and PDFs using Tesseract OCR with Khmer language support.

## Features

- **Web Interface**: Beautiful, responsive UI for uploading and processing files
- **REST API**: Flask-based API for OCR processing
- **Multi-format Support**: Process images (PNG, JPG, JPEG, GIF, BMP, TIFF) and PDF files
- **Language Selection**: Choose between English, Khmer, or both languages
- **Drag & Drop**: Easy file upload with drag-and-drop support
- **Download Results**: Download extracted text as a .txt file
- **Copy to Clipboard**: Quick copy functionality for extracted text

## Contents

- `app.py` — Flask web application with REST API
- `templates/index.html` — Modern, responsive web UI
- `image2text.py` — Standalone script for image OCR
- `pdf2text.py` — Standalone script for PDF OCR
- `images/` — Place image files here for standalone scripts
- `pdf/` — Place PDF files here for standalone scripts
- `output/` — Output text files from processing
- `uploads/` — Temporary storage for uploaded files (auto-cleaned)

## Prerequisites

1. **Python 3.8 or newer**

2. **Tesseract OCR** installed on your system:
   - Windows: Download from https://github.com/tesseract-ocr/tesseract
   - Default installation path: `C:\Program Files\Tesseract-OCR\tesseract.exe`
   - **Important**: Install Khmer language data (`khm.traineddata`) during installation or download it separately

3. **Poppler** (for PDF processing):
   - Windows: Download from https://github.com/oschwartz10612/poppler-windows/releases/
   - Extract and add the `bin` folder to your system PATH

## Installation

1. Clone or download this repository

2. Install Python dependencies:

```powershell
pip install -r requirements.txt
```

Or install individually:

```powershell
pip install Flask Flask-CORS pytesseract Pillow pdf2image Werkzeug
```

3. Verify Tesseract installation:
   - Make sure Tesseract is installed at `C:\Program Files\Tesseract-OCR\tesseract.exe`
   - If installed elsewhere, update the path in `app.py`:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r'YOUR_PATH_HERE\tesseract.exe'
     ```

## Usage

### Web Application (Recommended)

1. Start the Flask server:

```powershell
python app.py
```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Use the web interface:
   - Select your preferred OCR language (English, Khmer, or both)
   - Drag and drop a file or click to browse
   - Click "Extract Text" button
   - View, copy, or download the extracted text

### API Endpoints

#### Health Check
```
GET /api/health
```

#### OCR Processing
```
POST /api/ocr
Content-Type: multipart/form-data

Parameters:
- file: Image or PDF file
- lang: Language code (optional, default: "eng+khm")
  - "eng+khm" - English and Khmer
  - "khm" - Khmer only
  - "eng" - English only

Response:
{
  "success": true,
  "text": "Extracted text...",
  "filename": "original_filename.jpg",
  "output_file": "timestamp_output.txt"
}
```

#### Download Text File
```
GET /api/download/<filename>
```

### Standalone Scripts

1) OCR a single image:

```powershell
python image2text.py
# Output: text printed to console and saved to `output2.txt`
```

2) OCR a PDF:

```powershell
python pdf2text.py
# Output: intermediate images saved in `output_images/` and combined text in `output_text.txt`
```

## Configuration

### Tesseract Path

Update in `app.py` if needed:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Upload Settings

Modify in `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
```

### Supported File Types

```python
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'pdf'}
```

## Tips & Notes

- **Khmer OCR**: Ensure `khm.traineddata` is in Tesseract's `tessdata` folder
- **Better Results**: Use high-quality scans (300 DPI or higher) for better accuracy
- **Large PDFs**: Processing may take longer for multi-page PDFs
- **File Size**: Maximum upload size is 16MB (configurable)

## Troubleshooting

**"Tesseract not found" error:**
- Verify Tesseract installation
- Update `tesseract_cmd` path in `app.py`
- Add Tesseract to system PATH

**"PDF conversion failed":**
- Install Poppler
- Add Poppler's `bin` folder to system PATH
- Restart terminal/IDE after PATH changes

**"Khmer text is garbled":**
- Confirm `khm.traineddata` is installed
- Try increasing DPI (edit `dpi=300` in code)
- Check if the image/PDF has clear, readable Khmer text

**"Module not found" errors:**
- Reinstall dependencies: `pip install -r requirements.txt`
- Check if you're using the correct Python environment

**"Port 5000 already in use":**
- Change port in `app.py`: `app.run(port=5001)`

## Deployment

### Railway.app (Recommended - FREE!)

**Easiest deployment with full OCR support:**

1. Push your code to GitHub
2. Go to https://railway.app
3. Click "Deploy from GitHub repo"
4. Select your repository
5. Railway auto-detects Dockerfile and deploys!

**[See detailed Railway deployment guide](RAILWAY_DEPLOY.md)**

### Other Deployment Options

- **Render.com** - Free tier, Docker support, easy setup
- **Heroku** - Use with buildpacks (see `Procfile` and `Aptfile`)
- **Docker** - Use included `Dockerfile` for any container platform
- **VPS** - DigitalOcean, AWS EC2, Google Cloud, etc.

**Note about Vercel**: Vercel doesn't support Tesseract OCR. Only document extraction (DOCX, CSV, XLSX) will work. For full OCR functionality, use Railway, Render, or Docker deployment.

**[See complete deployment guide](DEPLOYMENT.md)**

## Contact

If you need help or want to connect:
- Email: phon.sobon02@gmail.com

## 📄 License

This project is open source and available for educational and commercial use.
