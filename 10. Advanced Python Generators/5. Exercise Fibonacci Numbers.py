# 5. Exercise Fibonacci Numbers


# def fib(n):
#     a = 0
#     b = 1
#     print(a)
#     print(b)

#     for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#         print(c)


# def fib(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         yield a
#         temp = a
#         a = b
#         b = temp + b


def fib(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


for i in fib(20):
    print(i)
