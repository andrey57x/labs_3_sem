def sort(lst, reverse=False):
    return sorted(lst, key=abs, reverse=reverse)


def sort_with_lambda(lst, reverse=False):
    return sorted(lst, key=lambda x: -x if x < 0 else x, reverse=reverse)


def task4():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    print(sort(data, True))
    print(sort_with_lambda(data, True))
