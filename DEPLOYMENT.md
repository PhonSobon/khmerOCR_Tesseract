# Khmer OCR API - Vercel Deployment Guide

## Important Limitations on Vercel

Vercel is a **serverless platform** with specific limitations for OCR applications:

### **What DOESN'T Work on Vercel:**

1. **Tesseract OCR** - Not available in Vercel's serverless environment
2. **PDF to Image conversion** - Requires Poppler (not available)
3. **Large file uploads** - Limited to 4.5MB body size
4. **File system storage** - Only `/tmp` directory (temporary)

### **What DOES Work on Vercel:**

- **DOCX text extraction** - ✓ Works
- **CSV data extraction** - ✓ Works  
- **XLSX/XLS data extraction** - ✓ Works
- **Web UI** - ✓ Works
- **API endpoints** - ✓ Works

## Recommended Alternatives for Full OCR Support

### Option 1: Deploy to a VPS/Cloud Server (Recommended)

**Best platforms for full OCR functionality:**

1. **DigitalOcean App Platform**
   - Full Linux environment
   - Can install Tesseract
   - Easy deployment from GitHub
   - $5/month

2. **Heroku**
   - Supports buildpacks for Tesseract
   - Free tier available (with limitations)
   - GitHub integration

3. **Railway.app**
   - Docker support
   - Easy Tesseract installation
   - Free tier available

4. **AWS EC2 / Google Cloud / Azure VM**
   - Full control
   - Can install any dependencies
   - More expensive

### Option 2: Use Cloud OCR APIs

Replace Tesseract with cloud OCR services:

- **Google Cloud Vision API** - Excellent accuracy, supports Khmer
- **AWS Textract** - Good for documents
- **Azure Computer Vision** - Supports multiple languages
- **Tesseract via Docker container** - Deploy to services like Cloud Run

## Current Vercel Deployment (Limited)

If you still want to deploy to Vercel with limited functionality:

### Files Created:
- `vercel.json` - Vercel configuration
- `.vercelignore` - Files to exclude from deployment

### What Works:
- Document text extraction (DOCX, CSV, XLSX)
- Web interface
- File uploads (up to 4.5MB)

### What Doesn't Work:
- Image OCR (Tesseract not available)
- PDF OCR (Poppler not available)

## Deploying to Heroku (Recommended Alternative)

### Step 1: Create Heroku-specific files

Create `Procfile`:
```
web: gunicorn app:app
```

Create `runtime.txt`:
```
python-3.12.0
```

Create `Aptfile` (for Tesseract):
```
tesseract-ocr
tesseract-ocr-eng
tesseract-ocr-khm
```

Add to `requirements.txt`:
```
gunicorn
```

### Step 2: Deploy to Heroku

```bash
# Install Heroku CLI
# Then:
heroku login
heroku create your-app-name
heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt
heroku buildpacks:add --index 2 heroku/python
git push heroku main
```

## Docker Deployment (Best Solution)

Create a `Dockerfile`:

```dockerfile
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-khm \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

Deploy to:
- **Railway.app** (easiest)
- **Google Cloud Run**
- **AWS ECS**
- **Azure Container Instances**

## Summary

**For your Khmer OCR application, I recommend:**

1. **Best option**: Deploy with Docker to Railway.app or Google Cloud Run
2. **Easiest option**: Use Heroku with buildpacks
3. **Free option**: Deploy to a free VPS (Oracle Cloud, etc.)
4. **Current Vercel deployment**: Only works for document extraction (not OCR)

Would you like help setting up deployment for any of these platforms?
