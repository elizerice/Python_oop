class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

  
    def info(self):
        return ""

  
    def describe(self):
        print(f"{self.name}, {self.info()}")


class Person(User):
    def __init__(self, name, birth_date):
        super().__init__(name)
        self.birth_date = birth_date

  
    def info(self):
        return f"Дата рождения: {self.birth_date}"

  
    def subscribe(self, user):
        pass


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

  
    def info(self):
        return f"Описание: {self.description}"
