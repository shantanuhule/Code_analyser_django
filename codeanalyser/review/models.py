# review/models.py
from django.db import models

class CodeSubmission(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    code = models.TextField()
    review_result = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
