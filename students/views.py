import random
from django.shortcuts import render, redirect
from django.views import View
from Question.models import Question, Option, Category, FinalResult
from .models import RandomQuestions
from .forms import AnswerForm
from .answers_module import Answer
from django.core.paginator import Paginator
from .page_number import Page
from .final_score import Score
from .question_module import ThisQuestion
from .form_function import FormMaker


class StudentView(View):

    def get(self, request):
        page = Page(request)

        num_page = page.current_page()
        if not bool(num_page):
            num_page = '1'
        if num_page == '1':
            questions = Question.objects.all()
            list_questions = [q for q in questions]
            random.shuffle(list_questions)

            for i in list_questions:
                RandomQuestions.objects.create(category=i.category.category_name,
                                               question_text=i.question_text,
                                               session_id=request.session)

            r_questions = RandomQuestions.objects.all()

        else:
            r_questions = RandomQuestions.objects.all()

        paginator = Paginator(r_questions, 1)
        paginated_questions = paginator.get_page(num_page)
        this_question = ThisQuestion(request)
        form = AnswerForm()
        for question in paginated_questions:
            this_question.next_question(question.question_text)
            options = Option.objects.filter(question__question_text=question.question_text)
            form_maker = FormMaker(options)
            form.fields['field'].label = this_question.current_question()
            form.fields['field'].choices = form_maker.options_maker()

        return render(request, 'students/students_view.html', {'form': form})

    def post(self, request):
        form = AnswerForm(data=request.POST)
        answer = Answer(request)
        page = Page(request)
        this_question = ThisQuestion(request)
        if form.is_valid():
            choice = form.cleaned_data.get('field')
            question = Question.objects.get(question_text=this_question.current_question())
            choice_ob = Option.objects.filter(question=question)
            selected_answer = choice_ob[int(choice) - 1]
            answer.add(question.question_text, selected_answer, selected_answer.score)
            num_page = page.current_page()
            next_page = int(num_page) + 1
            if next_page > Question.counter.count():
                page.next_page('1')
                RandomQuestions.objects.all().delete()
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
