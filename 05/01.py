old_print = print


def print_uppercase(*args):
    args_upcased = [str(arg).upper() for arg in args]
    old_print(*args_upcased)


print = print_uppercase
