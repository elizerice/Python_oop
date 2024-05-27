class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    def intersection(self, other):
        left = max(self.x, other.x)
        right = min(self.x + self.w, other.x + other.w)
        bottom = max(self.y, other.y)
        top = min(self.y + self.h, other.y + other.h)

        if left < right and bottom < top:
            return Rectangle(left, bottom, right - left, top - bottom)
        else:
            return None
