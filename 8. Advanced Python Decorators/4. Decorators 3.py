# Decorators 3

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("**************")
        func(*args, **kwargs)
        print("**************")
    return wrap_func

# This is called "dacorater pattern"


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


# a = my_decorator(hello)
# a('hi')

hello("hiii")
