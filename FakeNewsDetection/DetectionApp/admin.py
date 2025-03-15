from django.contrib import admin
from .models import NewsSubmission

@admin.register(NewsSubmission)
class NewsSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_text', 'prediction', 'submission_date')  # Columns to display in the admin list view
    search_fields = ('news_text', 'prediction')  # Enable search functionality
    list_filter = ('prediction', 'submission_date')  # Add filters for prediction and date


admin.site.site_header = "Fake News Detection Admin"  # Custom header
admin.site.site_title = "Admin Panel"  # Browser tab title
admin.site.index_title = "Welcome to the Fake News Detection Admin"  # Welcome text