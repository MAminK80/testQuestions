ANSWER_SESSION_ID = 'page'


class Page:

    def __init__(self, request):

        self.session = request.session
        page = self.session.get(ANSWER_SESSION_ID)

        if not page:
            page = self.session[ANSWER_SESSION_ID] = {}

        self.page = page

    def __iter__(self):
        page = self.page.copy()
        for item in page.values():
            yield item

    def next_page(self, p):
        if '0' not in self.page:
            self.page['0'] = {'next_page': '1'}
        self.page['0']['next_page'] = str(p)
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

    def current_page(self):
        if bool(self.page):
            return self.page['0']['next_page']
        else:
            return '1'

    def save(self):
        self.session.modified = True
