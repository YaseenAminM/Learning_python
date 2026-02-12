# 5. Python Built-in Modules

import random
from random import shuffle
import random as oulala

# help(random)
# print(dir(random))

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list)
random.shuffle(my_list)
print(my_list)

print(oulala.randint(0, 100))
