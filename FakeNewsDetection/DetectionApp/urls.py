from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_news, name='predict_news'),
    # path('predict/', views.predict_news, name='predict_news'),
    path("history/", views.history, name='history'),
]