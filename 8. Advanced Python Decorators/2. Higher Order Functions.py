# Higher Order Functions

# higher thay accept another function
def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func


# @decorator
# def hello():
#     pass
