from Question.models import Option, Question

ANSWER_SESSION_ID = 'answer'


class Answer:
    def __init__(self, request):

        self.session = request.session
        answer = self.session.get(ANSWER_SESSION_ID)

        if not answer:
            answer = self.session[ANSWER_SESSION_ID] = {}

        self.answer = answer

    def __iter__(self):
        answer = self.answer.copy()
        for item in answer.values():
            yield item

    def unique_id_generator(self, question_answer):
        return str(Question.objects.get(question_text=question_answer).id)

    def add(self, question_answer, selected_choice, choice_score):
        unique = self.unique_id_generator(question_answer)
        if unique not in self.answer:
            self.answer[unique] = {'question_answer': question_answer, 'selected_choice': str(selected_choice), 'choice_score': str(choice_score)}
        self.answer[unique]['selected_choice'] = str(selected_choice)
        self.answer[unique]['choice_score'] = str(choice_score)
        self.save()

    def delete(self):
        del self.session
        self.save()

    def save(self):
        self.session.modified = True

    def get_session(self):
        return str(self.session)

    def category_score(self, category):
        score = 0
        for item in self.answer.values():
            question = Question.objects.get(question_text=item['question_answer'])
            if question.category == category:
                score += int(item['choice_score'])
        return score
