# 🚀 Quick Deployment Commands

## 🚂 Deploy to Railway.app (EASIEST - 5 minutes)

### Step 1: Prepare Git
```bash
git add .
git commit -m "Deploy Khmer OCR to Railway"
git push origin main
```

### Step 2: Deploy on Railway
1. Go to https://railway.app
2. Click "Start a New Project"
3. Login with GitHub
4. Click "Deploy from GitHub repo"
5. Select `khmerOCR_Tesseract`
6. Wait 3-5 minutes
7. Click "Settings" → "Generate Domain"
8. **Done!** Your app is live! 🎉

**Cost:** FREE (500 hours/month)
**Features:** Full OCR support with Tesseract + Khmer

---

## 🎨 Deploy to Render.com (Alternative)

### Quick Deploy
```bash
git add .
git commit -m "Deploy to Render"
git push origin main
```

1. Go to https://render.com
2. New Web Service
3. Connect GitHub repo
4. Click "Create Web Service"
5. **Done!**

**Cost:** FREE (750 hours/month)

---

## 💜 Deploy to Heroku (Classic)

### Setup Buildpacks
```bash
heroku login
heroku create khmer-ocr-app
heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt
heroku buildpacks:add --index 2 heroku/python
git push heroku main
heroku open
```

**Cost:** FREE (limited hours) or $7/month

---

## 🐳 Docker (Local Testing)

### Build and Run
```bash
# Build
docker build -t khmer-ocr .

# Run
docker run -p 5000:5000 khmer-ocr

# Open browser
start http://localhost:5000
```

---

## 🌐 Deploy to Google Cloud Run

```bash
# Install gcloud CLI first
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Deploy
gcloud run deploy khmer-ocr \
  --source . \
  --platform managed \
  --region asia-southeast1 \
  --allow-unauthenticated
```

---

## 📦 Deploy to DigitalOcean App Platform

### Via GitHub
1. Go to https://cloud.digitalocean.com/apps
2. Click "Create App"
3. Connect GitHub repository
4. Select `khmerOCR_Tesseract`
5. Choose "Dockerfile"
6. Click "Launch App"

**Cost:** $5/month

---

## ⚡ Test Locally First

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Open browser
start http://localhost:5000
```

---

## 🔍 Check Deployment Status

### Railway
```bash
# View logs in Railway dashboard
# Or use Railway CLI:
railway logs
```

### Render
```bash
# Check logs in Render dashboard
```

### Heroku
```bash
heroku logs --tail
```

### Docker
```bash
docker logs <container_id>
```

---

## 🛠️ Environment Variables (if needed)

### Railway/Render Dashboard:
```
FLASK_ENV=production
MAX_CONTENT_LENGTH=16777216
```

### Heroku:
```bash
heroku config:set FLASK_ENV=production
heroku config:set MAX_CONTENT_LENGTH=16777216
```

---

## ✅ Verify Deployment

Test these features after deployment:
- [ ] Upload a PNG/JPG image → OCR works
- [ ] Upload a PDF → OCR works
- [ ] Upload DOCX → Text extraction works
- [ ] Upload CSV → Data extraction works
- [ ] Upload XLSX → Data extraction works
- [ ] Download extracted text
- [ ] Copy to clipboard

---

## 🆘 Troubleshooting

### Build Fails
```bash
# Check logs
railway logs  # or render logs, heroku logs
```

### App Crashes
```bash
# Check if all dependencies are in requirements.txt
# Verify Dockerfile syntax
# Check Python version compatibility
```

### OCR Not Working
```bash
# Verify Tesseract installation in container
docker exec -it <container> tesseract --version
```

---

## 📊 My Recommendation

**For your Khmer OCR app:**

1. **🥇 Best:** Railway.app (easiest + free)
2. **🥈 Great:** Render.com (more free hours)
3. **🥉 Good:** Heroku (established platform)

**Avoid:** Vercel (OCR doesn't work)

---

## 🎯 Just Deploy Now!

**Fastest method (Railway):**
```bash
# 1. Push to GitHub
git add . && git commit -m "Deploy" && git push

# 2. Go to railway.app
# 3. Click "Deploy from GitHub"
# 4. Select your repo
# 5. Done! ✅
```

**Time: 5 minutes**
**Cost: FREE**
**Result: Fully working OCR app**

---

Need help? Email: phon.sobon02@gmail.com
