class Button:
    def __init__(self):
        self._count = 0


    def click(self):
        self._count += 1


    def click_count(self):
        return self._count

  
    def reset(self):
        self._count = 0
