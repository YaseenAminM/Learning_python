# args and kwargs

# *args and **kwargs

def super_func(name, *args, i="hi", **kwargs):
    print(*args)
    print(kwargs)
    # return sum(args) + sum(kwargs.values())
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# Order of parameters:
# Rules: params, *args, default parameters, **kwargs
