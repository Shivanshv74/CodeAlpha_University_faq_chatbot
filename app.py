"""
==================================================
UNIVERSITY FAQ CHATBOT - USER INTERFACE
==================================================

This Streamlit app provides the web interface for the FAQ chatbot.
Users can ask questions and get answers in real-time.

The interface includes:
- Chat window with history
- User input box
- Confidence score display
- Matched FAQ reference
- About section in sidebar
"""

import streamlit as st
from chatbot import get_answer


# ==================================================
# PAGE CONFIGURATION
# ==================================================
# Configure the Streamlit page appearance

st.set_page_config(
    page_title="University FAQ Chatbot",
    page_icon="🤖",
    layout="centered"  # Center the content
)


# ==================================================
# STYLING - Custom CSS for better appearance
# ==================================================

st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 38px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# HEADER - Title and welcome message
# ==================================================

st.markdown(
    '<div class="main-title">🤖 University FAQ Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Ask questions about admission, fees, exams, scholarships and more.'
    '</div>',
    unsafe_allow_html=True
)


# ==================================================
# SESSION STATE INITIALIZATION
# ==================================================
# Streamlit clears the page on every interaction
# We use session_state to remember the chat history

if "messages" not in st.session_state:
    st.session_state.messages = []  # List to store chat messages


# ==================================================
# DISPLAY CHAT HISTORY
# ==================================================
# Show all previous messages in the conversation

for message in st.session_state.messages:
    with st.chat_message(message["role"]):  # "user" or "assistant"
        st.write(message["content"])


# ==================================================
# USER INPUT - Chat box
# ==================================================

user_question = st.chat_input(
    "Type your question here..."
)


# ==================================================
# PROCESS AND RESPOND TO USER QUESTION
# ==================================================

if user_question:
    # 1. Add user message to history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    # 2. Display user message in chat
    with st.chat_message("user"):
        st.write(user_question)

    # 3. Get answer from chatbot
    # get_answer returns: (answer, similarity_score, matched_question)
    answer, similarity, matched_question = get_answer(
        user_question
    )

    # 4. Add bot message to history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # 5. Display bot response
    with st.chat_message("assistant"):
        st.write(answer)

        # Show matching information in an expandable section
        with st.expander("🔍 Matching Information"):
            st.write(
                f"**Matched FAQ:** {matched_question}"
            )
            st.write(
                f"**Similarity Score:** {similarity:.2f}"
            )


# ==================================================
# SIDEBAR - About section
# ==================================================
# Additional information about the project

with st.sidebar:
    st.header("ℹ️ About")

    st.write(
        """
        This FAQ chatbot uses Natural Language Processing
        to understand user questions and find the most
        relevant answer from the FAQ dataset.
        """
    )

    st.divider()

    st.subheader("Technologies")

    st.write("🐍 Python")
    st.write("🧠 NLTK")
    st.write("📊 TF-IDF")
    st.write("📐 Cosine Similarity")
    st.write("🎨 Streamlit")

    st.divider()

    st.subheader("About This Project")

    st.write(
        """
        This project was developed as part of the
        CodeAlpha Artificial Intelligence Internship.
        """
    )
    st.write("🌐 Streamlit")

    st.divider()

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()