def field(items, *args):
    assert len(args) > 0
    result = []
    if len(args) == 1:
        for dct in items:
            if args[0] in dct and dct[args[0]] is not None:
                result.append(dct[args[0]])
    else:
        for dct in items:
            temp = dict()
            for key in args:
                if key in dct and dct[key] is not None:
                    temp[key] = dct[key]
            result.append(temp)
    return result


def task1():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))
