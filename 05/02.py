def check_password(func):
    right_password = "00"
    password = input("Введите пароль: ")
    if password == right_password:
        return func
    print("Неверный пароль")
    return lambda x: None

@check_password
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(7))
