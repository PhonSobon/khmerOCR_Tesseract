# 🚂 Deploy to Railway.app (Easiest & Free!)

Railway.app is perfect for your Khmer OCR application. It's **easy**, **free tier available**, and supports **Docker**.

## ✅ Why Railway?

- ✅ **Free tier** with 500 hours/month
- ✅ **Full Tesseract support**
- ✅ **Automatic HTTPS**
- ✅ **GitHub integration**
- ✅ **No credit card required for free tier**
- ✅ **Easy deployment in 5 minutes**

## 🚀 Quick Deployment Steps

### Step 1: Prepare Your Repository

Make sure you have these files (already created for you):
- ✅ `Dockerfile`
- ✅ `requirements.txt`
- ✅ `app.py`

### Step 2: Push to GitHub

```bash
# If not already initialized
git init
git add .
git commit -m "Ready for deployment"

# Create a new GitHub repository and push
git remote add origin https://github.com/YOUR_USERNAME/khmerOCR_Tesseract.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Railway

1. **Go to Railway.app**
   - Visit: https://railway.app
   - Click "Start a New Project"
   - Login with GitHub

2. **Deploy from GitHub**
   - Click "Deploy from GitHub repo"
   - Select your `khmerOCR_Tesseract` repository
   - Click "Deploy Now"

3. **Wait for Build**
   - Railway will automatically detect your Dockerfile
   - Build takes about 3-5 minutes
   - Watch the build logs

4. **Generate Domain**
   - Go to "Settings" tab
   - Scroll to "Domains"
   - Click "Generate Domain"
   - Your app will be available at: `https://your-app.up.railway.app`

### Step 4: Test Your Deployment

Visit your Railway URL and test:
- ✅ Upload an image → OCR should work!
- ✅ Upload a PDF → OCR should work!
- ✅ Upload DOCX, CSV, XLSX → Text extraction should work!

## 🎯 Alternative: Deploy to Render.com

Another excellent free option:

1. Go to https://render.com
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Render will auto-detect Docker
6. Click "Create Web Service"
7. Wait 5-10 minutes for deployment

## 🐳 Local Docker Testing

Before deploying, test locally:

```bash
# Build the image
docker build -t khmer-ocr .

# Run the container
docker run -p 5000:5000 khmer-ocr

# Open browser
# Visit: http://localhost:5000
```

## 💰 Cost Comparison

| Platform | Free Tier | OCR Support | Ease | Best For |
|----------|-----------|-------------|------|----------|
| **Railway** | 500 hrs/month | ✅ Yes | ⭐⭐⭐⭐⭐ | **Recommended!** |
| **Render** | 750 hrs/month | ✅ Yes | ⭐⭐⭐⭐⭐ | Great alternative |
| **Heroku** | Limited | ✅ Yes* | ⭐⭐⭐ | Needs buildpacks |
| **Vercel** | Unlimited | ❌ No | ⭐⭐⭐⭐⭐ | Not for OCR |
| **DigitalOcean** | $5/month | ✅ Yes | ⭐⭐⭐ | For production |

## 🔧 Environment Variables (Optional)

If you need to configure anything, add in Railway settings:

```
FLASK_ENV=production
MAX_CONTENT_LENGTH=16777216
```

## 📊 Monitoring

Railway provides:
- Real-time logs
- Resource usage metrics
- Deployment history
- Automatic SSL certificates

## ⚡ Quick Troubleshooting

**Build fails?**
- Check Dockerfile syntax
- Ensure requirements.txt is correct

**App crashes?**
- Check Railway logs
- Verify PORT environment variable

**OCR not working?**
- Tesseract should be installed via Dockerfile
- Check if Khmer language data is available

## 🎉 You're Done!

Your Khmer OCR app should now be live and accessible worldwide!

Share your deployed URL: `https://your-app.up.railway.app`

---

**Need help?** Open an issue or contact: phon.sobon02@gmail.com
