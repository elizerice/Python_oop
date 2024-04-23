class Selector:
    def __init__(self, nums):
        self.nums = nums


    def get_odds(self):
        return [num for num in self.nums if num % 2 != 0]


    def get_evens(self):
        return [num for num in self.nums if num % 2 == 0]
