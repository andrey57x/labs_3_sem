from lab_python_fp.gen_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.data = items
        self.itr = iter(self.data)
        self.repeat = []
        self.ignore_case = False
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        pass

    def __next__(self):
        nxt = next(self.itr)
        while nxt in self.repeat or type(nxt) is str and self.ignore_case and nxt.lower() in self.repeat:
            nxt = next(self.itr)
        else:
            if type(nxt) is str and self.ignore_case:
                self.repeat.append(nxt.lower())
            else:
                self.repeat.append(nxt)
        return nxt

    def __iter__(self):
        return self


def task3():
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(*Unique(data))
    data = gen_random(10, 1, 3)
    print(*Unique(data))
    print(*Unique(('aABbcC'[i] for i in range(6)), ignore_case=True))
