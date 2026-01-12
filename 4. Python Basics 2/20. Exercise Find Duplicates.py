# Exercise Find Duplicates

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set()
for letter in some_list:
    if some_list.count(letter) > 1 and (letter not in duplicates):
        duplicates.add(letter)

print(list(duplicates))
