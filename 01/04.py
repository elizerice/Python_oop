class OddEvenSeparator:
    def __init__(self):
        self._even = list()
        self._odd = list()
    def add_number(self, num):
        if num % 2 == 0:
            self._even.append(num)
        else:
            self._odd.append(num)
    def even(self):
        return self._even

    def odd(self):
        return self._odd
