import random


def gen_random(num_count, begin, end):
    return [random.randint(begin, end) for _ in range(num_count)]


def task2():
    print(*gen_random(5, 1, 3))
