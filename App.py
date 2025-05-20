import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

# Load trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Streamlit UI
st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("📰 Fake News Detection App")
st.markdown("This app predicts whether a news article is **FAKE** or **REAL** using Machine Learning.")

news_text = st.text_area("Enter News Article Content:", height=300)

if st.button("Predict"):
    if news_text.strip() == "":
        st.warning("Please enter some news text!")
    else:
        input_vector = vectorizer.transform([news_text])
        prediction = model.predict(input_vector)[0]

        if prediction == "FAKE":
            st.error("This news is predicted to be **FAKE**.")
        else:
            st.success("This news is predicted to be **REAL**.")
