# Decorators 3

def my_decorator(func):
    def wrap_func(x, y):
        print("**************")
        func(*args, **kwargs)
        print("**************")
    return wrap_func


@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)


hello("hello", "😍")
