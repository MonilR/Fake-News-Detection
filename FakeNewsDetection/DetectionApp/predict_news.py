from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# # Load your pre-trained model and vectorizer
# model = joblib.load('fake_news_model.pkl')
# vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Get the absolute path to the directory containing this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def predict_fake_news(news_text):
    try:
        # Load model and vectorizer using absolute paths
        model_path = os.path.join(BASE_DIR, 'fake_news_model.pkl')
        vectorizer_path = os.path.join(BASE_DIR, 'tfidf_vectorizer.pkl')
        
        # Load your pre-trained model and vectorizer
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)

        # Verify vectorizer is fitted
        if not hasattr(vectorizer, 'vocabulary_'):
            raise ValueError("Vectorizer not fitted! Missing vocabulary.")
            
        # Transform the input text using the vectorizer
        text_vectorized = vectorizer.transform([news_text])  #Author: Monil R. Prajapati

        # Predict using the model
        prediction = model.predict(text_vectorized)
        return "Real" if prediction[0] == 0 else "Fake"
    except Exception as e:
        return f"Error: {str(e)}"