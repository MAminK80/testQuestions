from django.conf import settings
from django.db import models


class RandomQuestions(models.Model):
    category = models.CharField(max_length=100)
    question_text = models.TextField(max_length=1000)
    session_id = models.CharField(max_length=200, editable=False)
