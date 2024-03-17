class Balance:
    def __init__(self):
        self._right_count = 0
        self._left_count = 0


    def add_right(self, weight):
        self._right_count += weight

  
    def add_left(self, weight):
        self._left_count += weight

  
    def result(self):
        if self._right_count > self._left_count:
            return "R"
        if self._right_count < self._left_count:
            return "L"
        else:
            return "="
