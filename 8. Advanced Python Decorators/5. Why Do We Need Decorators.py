# Why Do We Need Decorators


# Modules

from time import time

# @performance Decorators


def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()

        print(f'took {t2 - t1} ms')
        return result
    return wrapper


@performance
def long_time():
    for i in range(2000000):
        i*5


long_time()
