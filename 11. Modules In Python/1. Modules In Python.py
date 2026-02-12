# 1. Modules In Python

# import utility
from utility import multiply, divide
# from utility import *
import shopping.more_shopping.shopping_cart
from shopping.more_shopping import shopping_cart
from shopping.more_shopping.shopping_cart import buy

if __name__ == "__main__":
    print(multiply(2, 2))
    print(divide(25, 5))

    print(shopping.more_shopping.shopping_cart.buy('apple'))

    print("Card List : ", shopping_cart.buy("Banana"))
    print("Card List : ", buy("apple"))
    print("Card List : ", buy("Orange"))
    print(max([1, 2, 3]))
