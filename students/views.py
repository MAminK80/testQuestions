import random

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from . import final_score
from Question.models import Question, Option, Category, FinalResult
from .forms import AnswerForm
from .answers_module import Answer
from django.core.paginator import Paginator
from .page_number import Page
from .final_score import Score


class StudentView(View):
    j = 0
    choice_list = []
    questions = Question.objects.all()
    if bool(Question.objects.all()):
        questions_list = [question for question in questions]
        random.shuffle(questions_list)
    final_list = []

    def get(self, request):
        options_list = []
        my_list = []
        my_list.clear()
        options_list.clear()
        self.choice_list.clear()
        answer = Answer(request)
        page = Page(request)
        paginator = Paginator(self.questions_list, 1)
        num_page = page.current_page()
        if not bool(num_page):
            num_page = '1'
        if num_page == 1:
            answer.delete()
        paginated_questions = paginator.get_page(num_page)
        for question in paginated_questions:
            i = 0
            self.choice_list.append(question.question_text)
            options = Option.objects.filter(question=question)
            for option in options:
                i += 1
                options_list.append((str(i), option.text))
            my_list.append([question, options_list])
        form = AnswerForm()
        form.fields['field'].choices = my_list[0][1]
        form.fields['field'].label = my_list[0][0].question_text
        return render(request, 'students/students_view.html', {'form': form})

    def post(self, request):
        form = AnswerForm(data=request.POST)
        answer = Answer(request)
        page = Page(request)
        if form.is_valid():
            choice = form.cleaned_data.get('field')
            question = Question.objects.get(question_text=self.choice_list[0])
            choice_ob = Option.objects.filter(question=question)
            selected_answer = choice_ob[int(choice) - 1]
            answer.add(question.question_text, selected_answer, selected_answer.score)
            num_page = page.current_page()
            next_page = int(num_page) + 1
            if next_page > Question.counter.count():
                page.next_page('1')
                random.shuffle(self.questions_list)
                return redirect('score')
            page.next_page(str(next_page))
            return redirect('student_view')


class ShowScoreView(View):

    def get(self, request):
        answer = Answer(request)
        categories = Category.objects.all()
        score_class = Score(request)
        score = score_class.final_score(request)
        categories_scores = score_class.all_category_scores(categories, request)
        result = FinalResult.objects.last()
        return render(request, 'students/score_view.html',
                      {'answer': answer, 'score': score, 'categories_scores': categories_scores, 'result': result})


class CategoryView(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        answer = Answer(request)
        score_class = Score(request)
        score = score_class.category_final_score(category, request)
        return render(request, 'students/category_detail.html',
                      {'answer': answer, 'score': score, 'category': category})
