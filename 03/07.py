class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

  
    def __call__(self, x):
        result = 0
        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * (x ** i)
        return result

  
    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coefficients = [0] * max_len
        for i in range(max_len):
            self_coef = self.coefficients[i] if i < len(self.coefficients) else 0
            other_coef = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coefficients[i] = self_coef + other_coef
        return Polynomial(new_coefficients)
