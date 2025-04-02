from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load your pre-trained model and vectorizer
model = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')


def predict_fake_news(news_text):
    try:
        # Load your pre-trained model and vectorizer
        model = joblib.load('fake_news_model.pkl')
        vectorizer = joblib.load('tfidf_vectorizer.pkl')

        # Transform the input text using the vectorizer
        text_vectorized = vectorizer.transform([news_text])  #Author: Monil R. Prajapati

        # Predict using the model
        prediction = model.predict(text_vectorized)
        return "Real" if prediction[0] == 0 else "Fake"
    except Exception as e:
        return f"Error: {str(e)}"