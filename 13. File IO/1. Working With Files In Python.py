# 1. Working With Files In Python


my_file = open("test.txt", encoding="UTF-8")

# print(my_file)

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

print(my_file.readlines())


my_file.close()
