class Summator:
    def __init__(self, n):
        self.n = n
        self.num = 1

  
    def transform(self):
        self.n = self.n

  
    def sum(self):
        res = 0
        for i in range(self.n + 1):
            res += i ** self.num
        return res


class SquareSummator(Summator):
    def transform(self):
        self.num = 2


class CubeSummator(Summator):
    def transform(self):
        self.num = 3

