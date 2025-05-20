# 📰 Fake News Detection using Machine Learning

This project uses Natural Language Processing (NLP) and a PassiveAggressiveClassifier to detect whether a news article is **FAKE** or **REAL**. The model is trained on a labeled dataset and is deployed using **Streamlit** for real-time predictions.

---

## 🚀 Demo

🔗 [Live Demo on Streamlit (optional link)](https://share.streamlit.io/yourusername/fake-news-detector)

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Project Workflow](#-project-workflow)
- [How to Run](#-how-to-run)
- [Model Performance](#-model-performance)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

## 📖 Overview

The goal of this project is to detect fake news from text using machine learning. It classifies input news content as either **REAL** or **FAKE** based on a trained model.

---

## 🛠 Tech Stack

| Tool           | Purpose                             |
|----------------|-------------------------------------|
| Python         | Core programming language           |
| Scikit-learn   | ML model training                   |
| NLTK           | Natural language processing         |
| Streamlit      | Web application framework           |
| Jupyter Notebook | Development environment            |
| Pandas/Numpy   | Data manipulation                   |
| Joblib         | Model serialization                 |

---

## 📊 Project Workflow

1. **Dataset**: Fake and real news dataset from Kaggle  
2. **Preprocessing**:
   - Lowercasing
   - Removing stopwords
   - TF-IDF vectorization
3. **Model**:
   - `PassiveAggressiveClassifier` trained on 80% of the data
4. **Evaluation**:
   - Accuracy, confusion matrix
5. **Deployment**:
   - Streamlit frontend for user interaction

---

## 💻 How to Run

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/AceOfSpades-1710/Fake-News-Detector.git
cd Fake-News-Detector
