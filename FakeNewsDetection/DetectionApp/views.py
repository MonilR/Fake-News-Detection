from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .predict_news import predict_fake_news  # Assume you have a function to predict news

@csrf_exempt
def predict_news(request):  # This is the Django view function
    prediction = None
    if request.method == 'POST':
        news_text = request.POST.get('newsText', '')
        if news_text.strip():
            prediction = predict_fake_news(news_text)  # Call the renamed function
        else:
            prediction = "Error: Input text is empty."
    return render(request, 'index.html', {'prediction': prediction})