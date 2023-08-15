from django.shortcuts import render
from django.views.generic import TemplateView
from Question.models import Questionnaire


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        questionnaires = Questionnaire.objects.all()
        context = super(HomeView, self).get_context_data()
        context['questionnaires'] = questionnaires
        return context


