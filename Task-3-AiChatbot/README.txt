# 🤖 Smart AI Chatbot using TF-IDF and Cosine Similarity

## 📌 Project Overview

This project implements a simple AI-based chatbot using Natural Language Processing (NLP) techniques.

The chatbot matches user input with predefined questions using TF-IDF vectorization and cosine similarity to generate intelligent responses.

---

## 🛠 Technologies Used

- Python
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- String Processing

---

## 📂 How It Works

1. The chatbot loads a knowledge base from `knowledge.txt`.
2. The file contains alternating lines:
   - Question
   - Answer
3. User input is cleaned (lowercase + punctuation removal).
4. TF-IDF converts text into numerical vectors.
5. Cosine similarity is calculated between user input and stored questions.
6. The best matching answer is returned.

---

## 📄 Knowledge Base Format

Example `knowledge.txt`:

```
What is your name?
I am an AI chatbot.
How are you?
I am doing great!
What is Python?
Python is a programming language.
```

Each question must be followed by its answer.

---

## 🚀 How to Run

1. Install required library:

```
pip install scikit-learn
```

2. Make sure `knowledge.txt` is in the same folder.

3. Run the script:

```
python chatbot.py
```

4. Type your question.

Type `exit` to quit.

---

## 🧠 Core Concepts Used

- Text Cleaning
- TF-IDF Vectorization
- Cosine Similarity
- Information Retrieval

---

## 📊 Features

- Intelligent similarity matching
- Threshold-based response filtering
- Easy to extend knowledge base
- Lightweight NLP chatbot

---

## 🔮 Future Improvements

- Add GUI interface
- Add voice input/output
- Add conversation memory
- Deploy as web application (Flask / Streamlit)
- Improve NLP using advanced models

---

## 👨‍💻 Author

Harsh Kushwah  
AI & Python Developer