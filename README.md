Fake News/Reviews Detector

Overview
- This project builds an AI-ML model to detect fake news/reviews and deploys it as a web app using Django and Flask.
    
Features
- Detect fake news/reviews from input text.
- Web interface for user input.
- REST API for predictions (Flask).
- Cloud deployment (Heroku/AWS).
- Optional: Bulk predictions via CSV upload.
    
Tools
- ML/NLP: Python, Scikit-learn, TensorFlow, Hugging Face.
- Web: Django, Flask.
- Deployment: Docker, Heroku, AWS.
    
Getting Started
    
Prerequisites   
- Python 3.x
    
Install dependencies:   
- pip install django flask scikit-learn tensorflow nltk spacy   
    
Steps    
Clone the repo:    
- git clone <repository-url>    
    
Set up a virtual environment:    
- python -m venv env    
- source env/bin/activate  # On Windows: env\Scripts\activate    
    
Run Flask API:    
- python flask_api.py    

Run Django app:    
- python manage.py runserver    
    
Deployment    
- Deploy using Docker (optional) or host on Heroku/AWS.    

Contributing    
- Contributions are welcome! Open an issue or submit a PR.    

    
