import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib  # Import joblib for saving the model and vectorizer

# Download stopwords
import nltk
nltk.download('stopwords')

# Load the dataset
news_dataset = pd.read_csv(r'C:\Users\monil\Desktop\Graduate Project\Fake-News-Detection\resources\train.csv\train.csv')

# Replace null values with empty string
news_dataset = news_dataset.fillna('')

# Merge author name and news title
news_dataset['content'] = news_dataset['author'] + ' ' + news_dataset['title']

# Separate the data and label
X = news_dataset.drop(columns='label', axis=1)
Y = news_dataset['label']

# Stemming function
port_stem = PorterStemmer()

def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content

# Apply stemming to the 'text' column
news_dataset['content'] = news_dataset['content'].apply(stemming)

# Separate the data and label
X = news_dataset['content'].values
Y = news_dataset['label'].values

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
vectorizer.fit(X)
X = vectorizer.transform(X)

# Split the dataset into training and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Evaluate the model
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data:', training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy score of the test data:', test_data_accuracy)

# Save the trained model and vectorizer
joblib.dump(model, 'fake_news_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
print("Model and vectorizer saved successfully!")