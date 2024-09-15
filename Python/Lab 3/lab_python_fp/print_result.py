import functools


def print_result(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f'Function: {func.__name__}')
        result = func(*args,**kwargs)
        if type(result) is list:
            for i in result:
                print(i)
        elif type(result) is dict:
            for key, value in result.items():
                print(f'{key} = {value}')
        else:
            print(result)
        print()
        return result

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


def task5():
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
