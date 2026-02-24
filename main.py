import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Load dataset
data = pd.read_csv("spam.csv")

# Step 2: Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["Message"])

# Step 3: Output labels
y = data["Label"]

# Step 4: Train model
model = MultinomialNB()
model.fit(X, y)

# Take input from user
user_message = input("Enter your message: ")

msg_vector = vectorizer.transform([user_message])

prediction = model.predict(msg_vector)

print("Prediction:", prediction[0])
