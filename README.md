# 📩 Spam Message Detection using Machine Learning

## 📌 Project Overview
This is a beginner-friendly Machine Learning project built using **Python**.
The project detects whether a message is **Spam** or **Ham (Normal message)** using a supervised learning algorithm.

---

## 🎯 Objective
To classify SMS/text messages automatically as:
- **Spam** → unwanted or promotional messages
- **Ham** → normal messages

---

## 🧠 Machine Learning Concept
- **Type:** Supervised Learning
- **Algorithm:** Naive Bayes (MultinomialNB)
- **Text Processing:** CountVectorizer

---

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn

---

## 📂 Project Structure
Spam_Detection_Project
│
├── spam.csv # Dataset
├── main.py # Main Python code
└── README.md # Project documentation

---

## 📊 Dataset
The dataset contains example messages with labels:

| Message | Label |
|---|---|
| Win money now | spam |
| Hello how are you | ham |

The model learns patterns from these examples.

---

## ⚙️ How It Works
1. Load dataset using Pandas
2. Convert text into numbers using CountVectorizer
3. Train model using Naive Bayes algorithm
4. Take user input message
5. Predict whether message is spam or ham

---

## ▶️ How to Run the Project

### Install required libraries
```bash
pip install pandas scikit-learn

