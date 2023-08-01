from Question.models import Question

ANSWER_SESSION_ID = 'question'


class ThisQuestion:

    def __init__(self, request):

        self.session = request.session
        question = self.session.get(ANSWER_SESSION_ID)

        if not question:
            question = self.session[ANSWER_SESSION_ID] = {}

        self.question = question

    def __iter__(self):
        question = self.question.copy()
        for item in question.values():
            yield item

    def next_question(self, p):
        if '0' not in self.question:
            self.question['0'] = {'next_question': p}
        self.question['0']['next_question'] = p
        # if bool(self.page):
        # self.page['0']['next_page'] = str(p)
        # else:
        # self.page['0'] = {'next_page': '1'}
        self.save()

    def delete(self):
        # if unique in self.answer:
        # del self.answer[unique]
        del self.session
        self.save()

    def current_question(self):
        if bool(self.question):
            return self.question['0']['next_question']
        else:
            return Question.objects.first()

    def save(self):
        self.session.modified = True
