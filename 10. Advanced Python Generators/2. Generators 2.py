# 2. Generators 2

# iterable
# iterate
# generator

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result


def generator_function(num):
    for i in range(num):
        yield i


# for item in generator_function(100000):
#     print(item)

g = generator_function(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# this i will cause the error after the limit
# print(next(g))
# print(next(g))
