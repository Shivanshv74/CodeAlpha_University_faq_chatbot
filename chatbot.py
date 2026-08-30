"""
FAQ CHATBOT - THE AI BRAIN

This module contains the core NLP logic that powers the chatbot.
It loads FAQs, preprocesses text, and finds matching answers.
"""

import json
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data if needed
try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords")

# Load FAQ database
with open("faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)

# Load stopwords
STOP_WORDS = set(stopwords.words("english"))

def preprocess_text(text):
    """Clean and normalize text for NLP."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    words = text.split()
    words = [word for word in words if word not in STOP_WORDS]
    return " ".join(words)

# Preprocess all FAQ questions
faq_questions = [preprocess_text(faq["question"]) for faq in faqs]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
faq_vectors = vectorizer.fit_transform(faq_questions)

def get_answer(user_question):
    """Find and return the best matching FAQ answer."""
    processed = preprocess_text(user_question)
    
    if not processed.strip():
        return ("Please enter a question.", 0.0, "No question")
    
    user_vector = vectorizer.transform([processed])
    similarities = cosine_similarity(user_vector, faq_vectors)[0]
    
    best_index = similarities.argmax()
    best_score = similarities[best_index]
    matched_question = faqs[best_index]["question"]
    
    MINIMUM_SCORE = 0.15
    if best_score < MINIMUM_SCORE:
        return (
            "I'm sorry, I couldn't find a suitable "
            "answer to your question. Please try "
            "asking in a different way.",
            best_score,
            matched_question,
        )
    
    answer = faqs[best_index]["answer"]
    return (answer, best_score, matched_question)