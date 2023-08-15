class FormMaker:
    def __init__(self, options):
        self.options = options
        self.i = 0
        self.arr = []

    def options_maker(self):
        for option in self.options:
            self.i += 1
            self.arr.append((str(self.i), option.text))

        return self.arr
