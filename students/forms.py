from Question.models import Question, Option
from django import forms
from django.core.paginator import Paginator
import random


class AnswerForm(forms.Form):
    # page_number = forms.IntegerField()
    # print(page_number)

    # def __init__(self, *args, **kwargs):
    # self.page_number = forms.IntegerField()
    # exclude_fields = kwargs.pop('exclude', None)
    # super().__init__(*args, **kwargs)

    # if exclude_fields:
    # for field_name in exclude_fields:
    # self.fields.pop(field_name)

    choice_list = [('1', 'Amin'), ('2', 'Amin'), ('3', 'Amin'), ('4', 'Amin'), ('5', 'Amin'), ('6', 'Amin'), ('7', 'Amin'), ('8', 'Amin'), ('9', 'Amin'), ('10', 'Amin'), ('11', 'Amin'), ('12', 'Amin'), ('13', 'Amin'), ('14', 'Amin'), ('15', 'Amin')]
    field = forms.ChoiceField(choices=choice_list, widget=forms.RadioSelect(attrs={'class': ("formbold-radio-label", "formbold-radio-flex", "formbold-radio-group", "formbold-input-radio")}))
    # def __init__(self, *args, **kwargs):
    # questions = Question.objects.all()
    # self.page_number = forms.IntegerField()
    # paginator = Paginator(questions, 1)
    # paginated_questions = paginator.get_page(self.page_number)
    # choices = []
    # for question in questions:
    # choice_set = Option.objects.filter(question=question)
    # choices.append((question, str(question.pk), [(c.pk, c.text) for c in choice_set]))
    # super(AnswerForm, self).__init__(*args, **kwargs)
    # for question, question_pk, choice_list in choices:
    # self.question_text = question.question_text
    # self.fields[question_pk] = forms.ChoiceField(choices=choice_list, widget=forms.RadioSelect(),
    # label=self.question_text)

