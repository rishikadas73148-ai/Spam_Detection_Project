Spam Message Detection using Machine Learning





 Project Overview





This is a beginner-friendly Machine Learning project built using Python.



The project detects whether a message is Spam or Ham (Normal message) using a supervised learning algorithm.



 Objective





To classify SMS/text messages automatically as:



Spam → unwanted or promotional messages



Ham → normal messages



 Machine Learning Concept

Type: Supervised Learning



Algorithm: Naive Bayes (MultinomialNB)



Text Processing: CountVectorizer



 Technologies Used

Python



Pandas



Scikit-learn



Project Structure



Spam\_Detection\_Project

│

├── spam.csv # Dataset

├── main.py # Main Python code

└── README.md # Project documentation



 Dataset





The dataset contains example messages with labels:



Message



Label



Win money now



spam



Hello how are you



ham





The model learns patterns from these examples.



 How It Works

Load dataset using Pandas



Convert text into numbers using CountVectorizer



Train model using Naive Bayes algorithm



Take user input message



Predict whether message is spam or ham



 How to Run the Project





Install required libraries

pip install pandas scikit-learn



Run the program

python main.py



Example Output

Enter your message: Win free cash now



Prediction: spam



Learning Outcome

Basic understanding of Machine Learning



Text classification using Python



Working with datasets



Building a simple ML model

