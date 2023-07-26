from django.conf import settings
from django.db import models
from django.utils.text import slugify
import numpy as np


class FinalResult(models.Model):
    first_text = models.CharField(max_length=250)
    second_text = models.CharField(max_length=250)
    third_text = models.CharField(max_length=250)
    fourth_text = models.CharField(max_length=250)


class CategoryManager(models.Manager):
    def sum(self):
        importance = 0
        for category in self.all():
            importance += category.importance
        return importance


class Category(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, unique=True, blank=True)
    importance = models.IntegerField()
    sum_importance = CategoryManager()
    objects = models.Manager()
    first_text = models.CharField(max_length=250)
    second_text = models.CharField(max_length=250)
    third_text = models.CharField(max_length=250)
    fourth_text = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.category_name)
        super(Category, self).save()


class QuestionManager(models.Manager):
    def count(self):
        return len(self.all())


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='question')
    question_text = models.TextField(max_length=1000)
    counter = QuestionManager()
    objects = models.Manager()

    def __str__(self):
        return self.question_text


class OptionManager(models.Manager):
    def max_score(self, question):
        scores_list = []
        for option in self.filter(question=question):
            scores_list.append(option.score)
        scores_array = np.array(scores_list)
        return np.max(scores_array)


class Option(models.Model):
    text = models.CharField(max_length=300)
    score = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='option')
    max_score = OptionManager()
    objects = models.Manager()

    def __str__(self):
        return self.text
