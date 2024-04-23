class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []


    def add_word(self, word):
        if len(' '.join(self.words + [word])) <= self.width:
            self.words.append(word)
        else:
            self.end()
            self.words.append(word)


    def end(self):
        print(' '.join(self.words))
        self.words.clear()


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []


    def add_word(self, word):
        if len(' '.join(self.words + [word])) <= self.width:
            self.words.append(word)
        else:
            self.end()
            self.words.append(word)


    def end(self):
        spaces = self.width - sum(len(word) for word in self.words)
        print(' ' * spaces + ' '.join(self.words))
        self.words.clear()
