from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .forms import ContactUsForm

from .models import Questionnaire, ContactUs


class QuestionnaireListView(ListView):
    template_name = 'Question/question_list.html'
    model = Questionnaire


class ContactUsView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, 'Question/contact.html', {'form': form})

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'Question/contact.html', {'form': form})
