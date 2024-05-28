lass Profile:
    def __init__(self, profession):
        self.profession = profession


    def info(self):
        return ""


    def describe(self):
        print(f"{self.profession} {self.info()}")


class Vacancy(Profile):
    def __init__(self, profession, pay):
        super().__init__(profession)
        self.pay = pay

    def info(self):
        return f"Предлагаемая зарплата: {self.pay}"


class Resume(Profile):
    def __init__(self, profession, experience):
        super().__init__(profession)
        self.experience = experience

  
    def info(self):
        return f"Стаж работы: {self.experience}"
