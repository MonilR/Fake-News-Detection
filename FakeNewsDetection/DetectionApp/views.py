from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .predict_news import predict_fake_news
from .models import NewsSubmission  # Import the model

@csrf_exempt
def predict_news(request):
    prediction = None
    if request.method == 'POST':
        news_text = request.POST.get('newsText', '')
        if news_text.strip():
            prediction = predict_fake_news(news_text)  # Get prediction
            # Save the submission to the database
            NewsSubmission.objects.create(news_text=news_text, prediction=prediction)
        else:
            prediction = "Error: Input text is empty."
    return render(request, 'index.html', {'prediction': prediction})