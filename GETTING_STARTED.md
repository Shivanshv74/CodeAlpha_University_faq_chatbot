# 🚀 Getting Started Guide

Welcome! This guide will have you running the FAQ Chatbot in 5 minutes.

## ⚡ 5-Minute Quickstart

### Step 1: Download & Open (1 min)
1. Download/clone this project to your computer
2. Open the folder in your favorite terminal or file explorer

### Step 2: Run the Chatbot (2 min)

**Windows:** Double-click `run.bat`

**Mac/Linux:** Open terminal and run:
```bash
chmod +x run.sh
./run.sh
```

That's it! The chatbot will start automatically.

### Step 3: Open in Browser (30 sec)
- Automatic: Browser opens at `http://localhost:8502`
- Manual: Copy-paste `http://localhost:8502` in your browser

### Step 4: Start Chatting! (1.5 min)
Type your question in the chat box and press Enter.

---

## 💬 Example Questions to Try

### Admission Related
- "How can I apply for admission?"
- "What are the admission requirements?"
- "What documents do I need?"

### Fees & Payments
- "How much are the fees?"
- "Can I pay fees online?"
- "Payment methods?"

### Academic Calendar
- "When does the semester start?"
- "Where can I find the academic calendar?"

### Exams
- "How do I check my exam schedule?"
- "When will results be released?"
- "How can I download my admit card?"

### Scholarships
- "Are scholarships available?"
- "How do I apply for a scholarship?"

### Library
- "How can I access the library?"
- "What are library timings?"

### Other
- "Is attendance mandatory?"
- "How can I apply for leave?"
- "How can I contact the university?"

---

## 🎯 What You'll See

### Chat Interface
```
┌─────────────────────────────────────┐
│  🤖 University FAQ Chatbot          │
│  Ask questions about admission...   │
├─────────────────────────────────────┤
│                                     │
│ You: How can I apply?               │
│                                     │
│ Bot: You can apply through...       │
│                                     │
│ 🔍 Matching Information             │
│ Matched FAQ: How can I apply...     │
│ Similarity Score: 0.95              │
│                                     │
├─────────────────────────────────────┤
│ Type your question here...          │
│                                     │
└─────────────────────────────────────┘
```

### Sidebar Info
- About the project
- Technologies used
- Project details

---

## 🔧 Troubleshooting

### Issue: Nothing happens when I run the script
**Solution:** 
1. Make sure Python is installed: `python --version`
2. Make sure you're in the right folder
3. Try manual setup (see below)

### Issue: "Port 8502 is already in use"
**Solution:** Another app is using that port. Close it or run:
```bash
streamlit run app.py --server.port 8503
```

### Issue: "ModuleNotFoundError"
**Solution:** Dependencies not installed. Run:
```bash
pip install streamlit nltk scikit-learn
```

### Issue: Slow responses
**Solution:** This is normal on first run (NLTK downloads data). Wait 1-2 minutes.

---

## 🔄 Manual Setup (If Script Doesn't Work)

### Windows:
```batch
# Open Command Prompt in the project folder

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Mac/Linux:
```bash
# Open Terminal in the project folder

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📁 Project Files Explained

| File | What It Does |
|------|------------|
| `app.py` | Chat interface (what you see) |
| `chatbot.py` | AI brain (finds answers) |
| `faqs.json` | Q&A database |
| `requirements.txt` | List of packages needed |
| `run.bat` | Windows launcher |
| `run.sh` | Mac/Linux launcher |
| `.streamlit/config.toml` | Styling settings |
| `README.md` | Project info |
| `TECHNICAL_GUIDE.md` | How it works (technical) |
| `CODEALPHA_CHECKLIST.md` | Requirements verification |

---

## 🎓 Next Steps

### 1. **Understand the Code**
- Read `TECHNICAL_GUIDE.md` to understand how it works
- Look at `chatbot.py` comments to see the NLP pipeline
- Look at `app.py` to see how the UI works

### 2. **Customize It**
- **Add more FAQs:** Edit `faqs.json`
- **Change colors:** Edit `.streamlit/config.toml`
- **Change similarity threshold:** Edit `chatbot.py` line ~138

### 3. **Deploy It**
- **Easy (Streamlit Cloud):** Follow `DEPLOYMENT.md` - 5 min setup, free hosting
- **Advanced:** Docker, Heroku, AWS (see `DEPLOYMENT.md`)

### 4. **Improve It**
- Add user feedback system
- Expand FAQ database
- Use better NLP models (BERT)
- Add multiple language support

---

## ❓ Common Questions

### Q: Can I add more FAQ topics?
**A:** Yes! Edit `faqs.json` and add more Q&A pairs. Restart the app.

### Q: Will it understand typos?
**A:** Some typos yes, most no. The preprocessing helps, but very different spellings won't match.

### Q: Can I use this for my own product?
**A:** Absolutely! Just replace `faqs.json` with your Q&A pairs.

### Q: How do I make it faster?
**A:** More FAQs = slightly slower. Current setup with 26 FAQs is very fast.

### Q: Can I host it online for free?
**A:** Yes! Use Streamlit Cloud (free tier available). See `DEPLOYMENT.md`.

### Q: How do I share it with others?
**A:** 
- Locally: Send them this folder + run script
- Online: Deploy to Streamlit Cloud, share the URL

---

## 📞 Support

### For Technical Questions
- Read `TECHNICAL_GUIDE.md`
- Check `DEPLOYMENT.md` for deployment issues
- See code comments in `chatbot.py` and `app.py`

### For Improvements
- Modify `faqs.json` to add more Q&A
- Adjust settings in `.streamlit/config.toml`
- See "How to Modify & Extend" in `TECHNICAL_GUIDE.md`

---

## ✅ You're All Set!

You now have:
- ✅ A working FAQ chatbot
- ✅ Complete documentation
- ✅ Deployment guide
- ✅ Technical reference
- ✅ Customization guide

**Time to start chatting!** 🎉

```
Press Enter to close this guide and start the app.
```

---

**Made with ❤️ to make AI accessible to everyone**
