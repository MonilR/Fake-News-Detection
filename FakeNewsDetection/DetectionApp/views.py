from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .predict_news import predict_fake_news
from .models import NewsSubmission  # Import the model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

@login_required
@csrf_exempt
def predict_news(request):
    prediction = None
    if request.method == 'POST':
        news_text = request.POST.get('newsText', '')
        if news_text.strip():
            prediction = predict_fake_news(news_text)
            if not prediction.startswith("Error"):
                 # Save the submission with the logged-in user
                NewsSubmission.objects.create(user=request.user, news_text=news_text, prediction=prediction)
        else:
            prediction = "Error: Input text is empty."
    return render(request, 'index.html', {'prediction': prediction})


@login_required
def history(request):
    # Fetch submissions for the logged-in user, ordered by most recent
    submissions = NewsSubmission.objects.filter(user=request.user).order_by('-submission_date')
    return render(request, 'history.html', {'submissions': submissions})

def health_check(request):
    return HttpResponse("OK", status=200)