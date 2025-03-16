from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class NewsSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Associate with a user
    news_text = CKEditor5Field('Text', config_name='extends')  
    prediction = models.CharField(max_length=10)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.id} - {self.prediction} ({self.submission_date}"