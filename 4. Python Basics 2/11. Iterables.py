# Iterables

# for item in (1, 2, 3, 4, 5):
#     for x in ['a', 'b', 'c']:
#         print(item, x)

users = {
    "name": "Golem",
    "age": 5006,
    "can_swim": True
}

# print(users)

for key, value in users.items():
    print(key, " : ", value)

for key in users.keys():
    print(key)

for value in users.values():
    print(value)
