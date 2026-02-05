# Lambda Expressions
from functools import reduce

# lambda param: action(param)
my_list = [1, 2, 3]


def multiply_by_2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# print(reduce(accumulator, my_list, 0))
# using normal function
print(list(map(multiply_by_2, my_list)))
# using the lamba function
print(list(map(lambda item: item * 2, my_list)))
print(my_list)
# Filtering the date using the lambda function
print(list(filter(lambda item: item % 2 != 0, my_list)))
# reducing the data using the lambda function
print(reduce(lambda acc, item: acc + item, my_list, 0))
