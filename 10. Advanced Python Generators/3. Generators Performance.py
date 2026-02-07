# 3. Generators Performance

from time import time


# performance decorator
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         fn(*args, **kwargs)
#         t2 = time()
#         print(f"took : {t2 - t1}")
#     return wrapper

# @performance
# def long_time():
#     print('1')
#     for item in range(20000000):
#         item * 5

# @performance
# def long_time_2():
#     print('2')
#     for item in list(range(20000000)):
#         item * 5

# long_time()
# long_time_2()
# ###################################

# Generator Function
def gen_func(num):
    for i in range(num):
        yield i
