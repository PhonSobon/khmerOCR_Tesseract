# ⚠️ Vercel 404 Error - Why It Happens & How to Fix

## 🔴 The Problem

You're getting a **404 NOT_FOUND** error on Vercel because:

### 1. **Tesseract OCR Not Available**
Vercel runs on **AWS Lambda** (serverless), which doesn't include system binaries like:
- ❌ Tesseract OCR
- ❌ Poppler (for PDF conversion)
- ❌ Other system-level dependencies

### 2. **File System Limitations**
- Vercel only allows writing to `/tmp` (temporary storage)
- Files are deleted after each request
- Limited to 4.5MB payload size

### 3. **Lambda Environment**
- No persistent file storage
- No system package installation
- Read-only file system (except `/tmp`)

## ✅ The Solution: Use a Better Platform

### 🚂 **Option 1: Railway.app (RECOMMENDED)**

**Why Railway is perfect for your OCR app:**
- ✅ FREE tier (500 hours/month)
- ✅ Full Tesseract support
- ✅ Docker container support
- ✅ GitHub integration
- ✅ Automatic HTTPS
- ✅ **Takes 5 minutes to deploy!**

**How to deploy:**
```bash
# 1. Push to GitHub
git add .
git commit -m "Ready for Railway deployment"
git push origin main

# 2. Go to https://railway.app
# 3. Click "Deploy from GitHub"
# 4. Select your repo
# 5. Done! Your app is live!
```

📖 **[Full Railway Guide](RAILWAY_DEPLOY.md)**

---

### 🎨 **Option 2: Render.com**

**Similar to Railway:**
- ✅ FREE tier (750 hours/month)
- ✅ Docker support
- ✅ Auto-deploy from GitHub
- ✅ Free SSL

**How to deploy:**
1. Go to https://render.com
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your repository
5. Render auto-detects Dockerfile
6. Click "Create Web Service"

---

### 🐳 **Option 3: Docker + Cloud Run**

**For production apps:**
- Google Cloud Run
- AWS ECS
- Azure Container Instances

```bash
# Build and test locally
docker build -t khmer-ocr .
docker run -p 5000:5000 khmer-ocr

# Deploy to Cloud Run (example)
gcloud run deploy khmer-ocr --source .
```

---

### 💜 **Option 4: Heroku**

**Using buildpacks:**
- Uses `Procfile` (already created)
- Uses `Aptfile` for system packages
- Free tier available

```bash
heroku login
heroku create your-app-name
heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt
heroku buildpacks:add --index 2 heroku/python
git push heroku main
```

---

## 📊 Platform Comparison

| Platform | Setup Time | Free Tier | OCR Works | Best For |
|----------|-----------|-----------|-----------|----------|
| **Railway** | 5 min | 500 hrs/mo | ✅ | **Best choice!** |
| **Render** | 10 min | 750 hrs/mo | ✅ | Great alternative |
| **Heroku** | 15 min | Limited | ✅ | Classic option |
| **Vercel** | 2 min | Unlimited | ❌ | Only doc extraction |
| **DigitalOcean** | 20 min | $5/month | ✅ | Production |

---

## 🎯 What Works on Each Platform

### Vercel (Limited)
- ✅ DOCX text extraction
- ✅ CSV data extraction
- ✅ XLSX data extraction
- ❌ Image OCR (no Tesseract)
- ❌ PDF OCR (no Poppler)

### Railway/Render/Heroku/Docker (Full Features)
- ✅ Image OCR (all formats)
- ✅ PDF OCR
- ✅ DOCX extraction
- ✅ CSV extraction
- ✅ XLSX extraction
- ✅ Khmer language support
- ✅ Large file uploads

---

## 🚀 Quick Start (Railway)

**3 commands to deploy:**

```bash
# 1. Commit your changes
git add . && git commit -m "Deploy to Railway"

# 2. Push to GitHub
git push origin main

# 3. Go to Railway.app and click "Deploy from GitHub"
```

**That's it!** Your OCR app will be live in 3-5 minutes.

---

## 🔧 Files Already Created for You

For easy deployment, I've created:

- ✅ `Dockerfile` - For Docker/Railway/Render deployment
- ✅ `Procfile` - For Heroku deployment
- ✅ `Aptfile` - System dependencies for Heroku
- ✅ `runtime.txt` - Python version specification
- ✅ `vercel.json` - Vercel config (limited functionality)
- ✅ `.vercelignore` - Files to exclude from Vercel
- ✅ `requirements.txt` - All Python dependencies

**You're ready to deploy anywhere!**

---

## ❓ Which Platform Should I Choose?

### For Your Khmer OCR App:

**🏆 1st Choice: Railway.app**
- Easiest setup
- Free tier
- Full OCR support
- 5-minute deployment

**🥈 2nd Choice: Render.com**
- Very similar to Railway
- Slightly more free hours
- Great alternative

**🥉 3rd Choice: Heroku**
- Well-established
- More complex setup
- Still good option

**❌ Don't Use: Vercel**
- OCR won't work
- Only for static/serverless apps
- Wrong platform for your needs

---

## 📧 Need Help?

If you have questions about deployment:
- Email: phon.sobon02@gmail.com
- Open an issue on GitHub

---

## ✅ Summary

**The 404 error on Vercel is expected** because Vercel doesn't support the system dependencies (Tesseract, Poppler) that your OCR app needs.

**Solution:** Deploy to Railway.app instead - it's FREE, EASY, and FULLY SUPPORTS your OCR application!

👉 **[Start deploying to Railway now](RAILWAY_DEPLOY.md)**
