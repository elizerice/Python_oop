class MinMaxWordFinder:
    def __init__(self):
        self.sentences = []
        self.word_counts = {}

    def add_sentence(self, sentence):
        self.sentences.append(sentence)
        for word in sentence.split():
            word = word.strip()
            if word:
                self.word_counts[word] = self.word_counts.get(word, 0) + 1

    def shortest_words(self):
        min_length = float('inf')
        for word, count in self.word_counts.items():
            if len(word) < min_length:
                min_length = len(word)
        return sorted([word for word, count in self.word_counts.items() if len(word) == min_length])

    def longest_words(self):
        max_length = 0
        for word in self.word_counts:
            if len(word) > max_length:
                max_length = len(word)
        return sorted(set([word for word, count in self.word_counts.items() if len(word) == max_length]), reverse=True)
