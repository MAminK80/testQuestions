import numpy as np
from Question.models import Option, Category, Question
from students.answers_module import Answer


class Score:
    def __init__(self, request):
        pass

    def category_final_score(self, category, request):
        max_scores = []
        answer = Answer(request)
        questions = Question.objects.filter(category=category)
        for question in questions:
            max_score = Option.max_score.max_score(question)
            max_scores.append(max_score)
        answer_scores = answer.category_score(category)
        final_score_category = (answer_scores/np.sum(max_scores)) * 100
        return int(final_score_category)

    def final_score(self, request):
        categories = Category.objects.all()
        score = []
        for category in categories:
            score.append(self.category_final_score(category, request) * category.importance)
        sum_importance = Category.sum_importance.sum()
        return int(np.sum(score) / sum_importance)

    def all_category_scores(self, categories, request):
        scores = []
        for category in categories:
            scores.append((category, self.category_final_score(category, request)))
        return scores

