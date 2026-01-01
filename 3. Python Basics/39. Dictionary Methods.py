
# Dictionary Methods
user = {
    "basket": [1, 2, 3],
    "greeting": 'hello'
}
print(user)
print(user['greeting'])

# This how we should handle the missing data by getting None
print(user.get("age"))


# Set a default value if age does'nt exists
print(user.get("age", 55))


# user2 = dict(key=value)

user2 = dict(name="Yaseen")
print(user2)
