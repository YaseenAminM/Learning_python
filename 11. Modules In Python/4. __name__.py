# __name__

from utility import multiply, divide
from shopping.more_shopping.shopping_cart import buy

# print(__name__)


class Student():
    pass


st1 = Student()
print(type(st1))  # <class '__main__.Student'>

if __name__ == '__main__':
    print("please run this...")
