# 🚀 Deployment Guide

This guide explains how to deploy the University FAQ Chatbot to various platforms.

## Table of Contents

1. [Local Deployment](#local-deployment)
2. [Streamlit Cloud Deployment](#streamlit-cloud-deployment)
3. [Heroku Deployment](#heroku-deployment)
4. [Docker Deployment](#docker-deployment)

---

## Local Deployment

### Prerequisites
- Python 3.8+
- Git

### Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd codealpha_FAQ_chatbot
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Application**
   ```bash
   streamlit run app.py
   ```

6. **Access Application**
   - Open browser: `http://localhost:8502`

---

## Streamlit Cloud Deployment (FREE & EASIEST)

Streamlit Cloud is the **easiest** and **free** way to deploy your app.

### Prerequisites
- GitHub account
- Streamlit account (sign up at https://share.streamlit.io)

### Steps

1. **Push Code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/codealpha_FAQ_chatbot.git
   git push -u origin main
   ```

2. **Sign Up for Streamlit Cloud**
   - Go to https://share.streamlit.io
   - Sign in with GitHub
   - Click "New app"

3. **Configure Deployment**
   - **Repository**: Select your GitHub repository
   - **Branch**: `main`
   - **Main file path**: `app.py`

4. **Deploy**
   - Click "Deploy"
   - Streamlit will automatically deploy your app
   - Get a shareable URL like: `https://your-app-name.streamlit.app`

5. **Manage Settings**
   - Go to settings (gear icon)
   - Configure rerun behavior, timezone, etc.

### Advantages
- ✅ **Free hosting**
- ✅ **Automatic deployments** from GitHub
- ✅ **Custom domain support**
- ✅ **No configuration needed**
- ✅ **Built-in SSL/HTTPS**

### Limitations
- Shared resources (slower than dedicated servers)
- Community tier has usage limits

---

## Heroku Deployment

### Prerequisites
- Heroku account (https://www.heroku.com)
- Git
- Heroku CLI

### Setup Files

Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

Create `.slugignore`:
```
__pycache__
.git
.gitignore
.venv
venv
```

Update `requirements.txt`:
```
streamlit>=1.30.0
nltk>=3.8
scikit-learn>=1.3.0
```

### Steps

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

3. **Set Build Pack**
   ```bash
   heroku buildpacks:set heroku/python
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

5. **View Logs**
   ```bash
   heroku logs --tail
   ```

### Note
Heroku's free tier was discontinued. You'll need a paid plan (starting at $5/month).

---

## Docker Deployment

### Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8502

CMD ["streamlit", "run", "app.py", "--server.port=8502", "--server.address=0.0.0.0"]
```

### Build and Run

```bash
# Build image
docker build -t faq-chatbot:latest .

# Run container
docker run -p 8502:8502 faq-chatbot:latest

# Run with volume mount (for live editing)
docker run -p 8502:8502 -v $(pwd):/app faq-chatbot:latest
```

### Deploy to Docker Hub

```bash
# Tag image
docker tag faq-chatbot:latest username/faq-chatbot:latest

# Login to Docker Hub
docker login

# Push image
docker push username/faq-chatbot:latest
```

---

## Performance Optimization

### 1. **Enable Caching**
```python
import streamlit as st

@st.cache_data
def load_faqs():
    # Load FAQs from file
    return faqs
```

### 2. **Lazy Load NLTK Data**
```python
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords', quiet=True)
```

### 3. **Use Requirements Pinning**
Pin specific versions for production:
```txt
streamlit==1.36.0
nltk==3.9.1
scikit-learn==1.5.0
```

---

## Monitoring & Maintenance

### Streamlit Cloud
- Check deployment logs in Streamlit Cloud dashboard
- Set up email notifications for errors
- Monitor app metrics

### Custom Server
- Use monitoring tools like Sentry for error tracking
- Set up log aggregation
- Monitor server resources

---

## Troubleshooting

### Issue: "ModuleNotFoundError" on deployment

**Solution**: Ensure all dependencies are in `requirements.txt`
```bash
pip freeze > requirements.txt
```

### Issue: App runs locally but fails on cloud

**Solution**: 
- Check file paths (use relative paths)
- Verify all data files are included
- Check Python version compatibility

### Issue: Slow response time

**Solution**:
- Enable caching with `@st.cache_data`
- Optimize TF-IDF vectorization
- Use lazy loading

### Issue: Port binding error

**Solution**: Update Streamlit config:
```toml
[server]
port = 8502
address = 0.0.0.0
```

---

## Recommended Deployment

For your internship project, **Streamlit Cloud** is recommended because:

1. ✅ **Free hosting**
2. ✅ **Easy setup** (just push to GitHub)
3. ✅ **Professional URL**
4. ✅ **Automatic updates**
5. ✅ **Shareable with reviewers**

**Time to deploy: ~5 minutes**

---

## Share Your App

Once deployed, share the link with:
- Reviewers
- Instructors
- Team members
- Stakeholders

Example: `https://your-app-name.streamlit.app`

---

**Happy Deploying! 🎉**
