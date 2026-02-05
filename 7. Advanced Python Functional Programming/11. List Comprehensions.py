# 11. List Comprehensions

# List, Set, Dictionary

my_list = []
# for char in "hello":
#     my_list.append(char)

# print(my_list)

# List Comprehension in action
my_new_list = [param for param in "hello"]
my_new_list_2 = [num for num in range(0, 10)]
my_new_list_3 = [num * 2 for num in range(1, 10)]
my_new_list_4 = [num**2 for num in range(1, 10) if num % 2 == 0]
print(my_new_list_4)
