# Sets

# my_set = {1, 1, 2, 2, 3, 3, }
my_list = [1, 2, 3, 4, 5, 5]
my_set = {1, 2, 3, 4, 5, 5}

# print(my_set)
# print(type(my_set))

my_set.add(100)
my_set.add(2)

print(my_set)
print(set(my_list))

print(1 in my_set)

new_set = my_list.copy()
print(new_set)
