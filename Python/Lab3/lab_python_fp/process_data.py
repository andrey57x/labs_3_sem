import json
import sys
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1


@print_result
def f1(arg):
    result = sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=lambda s: s.lower())
    return result


@print_result
def f2(arg):
    result = list(filter(lambda s: s.lower().startswith('программист'), arg))
    return result


@print_result
def f3(arg):
    result = list(map(lambda s: s + ' с опытом работы Python', arg))
    return result


@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100_000, 200_000)
    result = []
    for job, salary in zip(arg, salaries):
        result.append(job+f', зарплата {salary} руб.')
    return result


def task7():
    path = 'data_light.json'
    with open(path, encoding='utf8') as f:
        data = json.load(f)
    with cm_timer_1():
        f4(f3(f2(f1(data))))
