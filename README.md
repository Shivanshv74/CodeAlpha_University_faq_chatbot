# 🤖 University FAQ Chatbot

A Natural Language Processing based FAQ chatbot developed as part of the **CodeAlpha Artificial Intelligence Internship**.

## 📌 Project Overview

The University FAQ Chatbot is an intelligent question-answering system that helps students find answers to common university-related questions. Using advanced NLP techniques, it processes user queries and matches them with the most relevant FAQ entries from a comprehensive database.

The chatbot covers topics including:
- **Admission** - Application process, requirements, documents
- **Fees & Payments** - Tuition fees, payment methods
- **Academic Calendar** - Semester dates, important dates
- **Examinations** - Exam schedules, results, backlogs
- **Attendance & Leave** - Attendance policies, leave applications
- **Library Services** - Access, timings, resources
- **Scholarships** - Eligibility, application process
- **Student Support** - Contact information, student services

## ✨ Features

✅ **Natural Language Processing**
- Text preprocessing and normalization
- Stopword removal using NLTK
- TF-IDF vectorization for semantic analysis

✅ **Intelligent Matching**
- Cosine similarity-based matching
- N-gram support (1-2 grams)
- Confidence scoring system

✅ **User Experience**
- Interactive chat interface using Streamlit
- Real-time question processing
- Chat history tracking
- Similarity score display
- Matched FAQ reference

✅ **Robust Error Handling**
- Unknown question detection
- Minimum confidence threshold
- Graceful fallback messages

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **NLP** | NLTK |
| **ML/ML** | Scikit-learn |
| **Web Framework** | Streamlit |
| **Data Format** | JSON |

## 📋 Requirements

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Quick Start

### Option 1: Automatic Setup (Recommended)

**Windows:**
```bash
run.bat
```

**Mac/Linux:**
```bash
chmod +x run.sh
./run.sh
```

### Option 2: Manual Setup

1. **Clone or download the repository**
   ```bash
   cd codealpha_FAQ_chatbot
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser**
   - The app will automatically open at `http://localhost:8502`
   - Or manually navigate to the URL shown in the terminal

## 📂 Project Structure

```
codealpha_FAQ_chatbot/
├── app.py                 # Main Streamlit application
├── chatbot.py            # NLP and FAQ matching logic
├── faqs.json             # FAQ database (26 Q&A pairs)
├── requirements.txt      # Python dependencies
├── run.bat               # Windows launcher script
├── run.sh                # Mac/Linux launcher script
├── .gitignore            # Git ignore file
├── README.md             # This file
└── python --version.py   # Utility script
```

## 🧠 How It Works

### 1. **Question Input**
User enters a question in the chat interface.

### 2. **Text Preprocessing**
- Convert to lowercase
- Remove punctuation and special characters
- Split into words
- Remove English stopwords (the, is, a, etc.)

### 3. **Vectorization**
- FAQ questions and user question are converted to TF-IDF vectors
- Uses unigrams and bigrams for better context capture

### 4. **Similarity Matching**
- Cosine similarity is calculated between user question and all FAQ questions
- Identifies the most similar FAQ entry

### 5. **Confidence Scoring**
- Similarity scores range from 0.0 to 1.0
- Minimum threshold of 0.15 to filter poor matches
- User sees the confidence score and matched question

### 6. **Response Generation**
- Returns the corresponding FAQ answer
- Displays matching information (original FAQ, similarity score)
- Handles unknown questions gracefully

## 📊 Algorithm Details

```
Algorithm: TF-IDF Cosine Similarity Matching

Input: User Question Q
Output: Answer, Similarity Score, Matched Question

Steps:
1. FAQ_Questions = Load all FAQ questions from JSON
2. Preprocess Q and all FAQ_Questions
3. Create TF-IDF vectorizer with ngram_range=(1, 2)
4. vectors_FAQ = Vectorizer.fit_transform(FAQ_Questions)
5. vector_Q = Vectorizer.transform([Q])
6. similarities = cosine_similarity(vector_Q, vectors_FAQ)
7. best_index = argmax(similarities)
8. best_score = max(similarities)
9. IF best_score >= 0.15 THEN
     RETURN FAQ[best_index].answer, best_score, FAQ[best_index].question
   ELSE
     RETURN "Could not find answer", best_score, FAQ[best_index].question
```

## 💡 Example Usage

**User Input:**
```
How can I apply for admission?
```

**Chatbot Output:**
```
You can apply for admission through the university's official 
admission process. Check the admission portal for application details.

Matched FAQ: How can I apply for admission?
Similarity Score: 0.95
```

**User Input (Unknown Question):**
```
What is the meaning of life?
```

**Chatbot Output:**
```
I'm sorry, I couldn't find a suitable answer to your question. 
Please try asking in a different way.

Matched FAQ: How can I contact the university?
Similarity Score: 0.08
```

## 📈 Performance Metrics

- **FAQ Database Size:** 26 Q&A pairs
- **Response Time:** ~100-200ms per query
- **Accuracy:** Depends on question similarity to existing FAQs
- **Memory Usage:** ~50MB (including model)

## 🔧 Configuration

### Adjusting Similarity Threshold

Edit `chatbot.py` line ~138:
```python
MINIMUM_SCORE = 0.15  # Adjust this value (0.0 to 1.0)
```

- **Lower values:** More answers, possibly irrelevant
- **Higher values:** Fewer answers, only very relevant matches

### Expanding FAQ Database

Edit `faqs.json` to add more Q&A pairs:
```json
{
    "question": "Your question here?",
    "answer": "Your answer here."
}
```

## 🚀 Future Enhancements

- [ ] Add user feedback/rating system
- [ ] Implement learning from user interactions
- [ ] Support for multiple languages
- [ ] Advanced NLP with transformer models (BERT, GPT)
- [ ] Database integration for dynamic FAQs
- [ ] Export chat history feature
- [ ] Admin dashboard for managing FAQs
- [ ] Integration with university information systems
- [ ] Mobile app version
- [ ] Voice input/output support

## 📝 License

This project is part of the CodeAlpha AI Internship program.

## 👨‍💻 About CodeAlpha

CodeAlpha is an AI/ML internship program focused on practical projects and real-world applications.

## 📧 Support & Feedback

For issues, questions, or suggestions, please refer to the project repository or contact the development team.

---

**Made with ❤️ for the CodeAlpha Internship Program**