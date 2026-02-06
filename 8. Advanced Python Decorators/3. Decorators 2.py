# Decorators 2
def my_decorator(func):

    def wrap_func():
        print("**************************************")
        func()
        print("**************************************")
    return wrap_func

# def hello():
#     print("Helloooo...")

# greet = my_decorator(hello)
# greet()


@my_decorator
def hello():
    print("Helloooo...")


@my_decorator
def bye():
    print("see ya later.")


hello()
bye()

hello2 = my_decorator(hello)
hello2()
