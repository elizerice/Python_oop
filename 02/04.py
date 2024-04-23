class MinStat:
    def __init__(self):
        self.values = []

    def add_number(self, num):
        self.values.append(num)

    def result(self):
        if self.values:
            return min(self.values)
        else:
            return None


class MaxStat:
    def __init__(self):
        self.values = []

    def add_number(self, num):
        self.values.append(num)

    def result(self):
        if self.values:
            return max(self.values)
        else:
            return None


class AverageStat:
    def __init__(self):
        self.values = []

    def add_number(self, num):
        self.values.append(num)

    def result(self):
        if self.values:
            return sum(self.values) / len(self.values)
        else:
            return None
