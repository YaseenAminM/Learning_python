# 9. is vs ==

# print(True == 1)
# print('' == 1)
# print([] == 1)
# print(10 == 10.0)
# print([] == [])
# print([1, 2, 3] == [1, 2, 3])
# print("1" == 1)


# is compares the memory address (identity) of objects, not their values.

print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])
print([1, 2, 3] is [1, 2, 3])
print("1" is 1)

print(True is True)


a = [1, 2, 3]
b = [1, 2, 3]

print(a is [1, 2, 3])
print(a is b)
# print(a == b)
