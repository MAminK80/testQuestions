from Question.models import Question, Option
from django import forms
from django.core.paginator import Paginator
import random


class AnswerForm(forms.Form):
    choice_list = [('1', 'Amin'), ('2', 'Amin'), ('3', 'Amin'), ('4', 'Amin'), ('5', 'Amin'), ('6', 'Amin'),
                   ('7', 'Amin'), ('8', 'Amin'), ('9', 'Amin'), ('10', 'Amin'), ('11', 'Amin'), ('12', 'Amin'),
                   ('13', 'Amin'), ('14', 'Amin'), ('15', 'Amin')]
    field = forms.ChoiceField(choices=choice_list, widget=forms.RadioSelect(attrs={
        'class': ("formbold-radio-label", "formbold-radio-flex", "formbold-radio-group", "formbold-input-radio")}))
