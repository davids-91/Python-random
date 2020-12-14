import random


def random_numbers(start, end):
    x = random.randint(start, end)
    print(x)
    return x


def is_in_range(start, end):
    random_number = random_numbers(start, end)
    if start < random_number < end:
        return True
    else:
        return False
