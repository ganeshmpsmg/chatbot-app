import re
import streamlit as st
import nltk
from nltk.corpus import wordnet as wn

# Download required NLTK data (important for Streamlit Cloud)
nltk.download("wordnet")
nltk.download("omw-1.4")

# ------------------ Intent Definitions ------------------
intents = {
    "lost_item": {
        "keywords": {"lost", "missing", "misplaced", "stolen", "found"},
        "response": "Please report the lost item and check the nearest lost-and-found."
    },
    "lost_card": {
        "keywords": {"card", "credit", "debit"},
        "response": "Please block your card immediately and request a new one."
    },
    "greeting": {
        "keywords": {"hello", "hi", "hey", "morning", "evening"},
        "response": "Hello! How can I help you today?"
    },
    "time_query": {
        "keywords": {"time", "best", "morning", "evening", "night"},
        "response": "Early morning or evening is the best time."
    },
    "goodbye": {
        "keywords": {"bye", "exit", "quit", "goodbye"},
        "response": "Thank you! Have a great day."
    }
}

# ------------------ NLP Utilities ------------------
def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return set(text.split())

def expand_with_synonyms(tokens):
    expanded = set(tokens)
    for token in tokens:
        for syn in wn.synsets(token):
            for lemma in syn.lemmas():
                expanded.add(lemma.name().lower())
    return expanded

def get_response(user_input):
    tokens = tokenize(user_input)
    expanded_tokens = expand_with_synonyms(tokens)

    scores = {
        intent: len(expanded_tokens & data["keywords"])
        for intent, data in intents.items()
    }

    best_intent = max(scores, key=scores.get)

    if scores[best_intent] > 0:
        return intents[best_intent]["response"]
    return "Sorry, I couldn’t understand your request. Please rephrase."

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="Rule-Based Chatbot", layout="centered")

st.title("🤖 Rule-Based NLP Chatbot")
st.write("Ask me something using natural English")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", placeholder="Type your message here...")

if st.button("Send") and user_input:
    bot_response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")

