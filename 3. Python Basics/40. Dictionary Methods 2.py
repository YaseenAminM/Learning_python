# Dictionary Methods 2


user = {
    "basket": [1, 2, 3],
    "greeting": "hello",
    "age": 20
}


# print(user)


# 'i' in "hi"

# print("basket" in user)
# print("size" in user)

print("age" in user.keys())
print("hello" in user.values())
# print(user.items())

user2 = user.copy()
# print(user)
# print(user2)

# user.clear()
# print(user)

# user.pop('age')
# user.popitem()


user.update({'age': 26})

print(user)
