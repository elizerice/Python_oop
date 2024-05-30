class Summator:
    def __init__(self, n=1):
        self.n = n

    def transform(self, num):
        return num

    def sum(self, n):
        res = 0
        for i in range(n + 1):
            res += self.transform(i)
        return res


class PowerSummator(Summator):
    def __init__(self, degree):
        super().__init__()
        self.degree = degree

  
    def transform(self, num):
        return num ** self.degree


class SquareSummator(PowerSummator):
    def __init__(self, degree=2):
        super().__init__(degree)


class CubeSummator(PowerSummator):
    def __init__(self, degree=3):
        super().__init__(degree)

