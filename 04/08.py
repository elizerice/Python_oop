class Summator:
    def __init__(self, n):
        self.n = n
        self.degree = 1

    
    def transform(self):
        self.n = self.n

    
    def sum(self):
        res = 0
        for i in range(self.n + 1):
            res += i ** self.degree
        return res


class SquareSummator(Summator):
    def transform(self):
        self.degree = 2


class CubeSummator(Summator):
    def transform(self):
        self.degree = 3
