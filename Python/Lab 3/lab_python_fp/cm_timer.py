import time
import contextlib


class cm_timer_1:
    def __enter__(self):
        self.timer = time.time()

    def __exit__(self, *args):
        print(time.time() - self.timer)


@contextlib.contextmanager
def cm_timer_2():
    timer = time.time()
    yield
    print(time.time() - timer)


def task6():
    with cm_timer_1():
        time.sleep(0.5)
    with cm_timer_2():
        time.sleep(0.5)
