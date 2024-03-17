class BigBell:
    def __init__(self):
        self._sound = True

    def sound(self):
        if self._sound:
            print('ding')
        else:
            print('dong')
        self._sound = not self._sound
