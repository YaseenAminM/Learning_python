# Exercise Comprehensions
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dubbles = list(set([char for char in some_list if some_list.count(char) > 1]))
print(dubbles)
# print(some_list.count('b'))
