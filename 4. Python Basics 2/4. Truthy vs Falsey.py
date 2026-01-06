# Truthy vs Falsey


is_old = True
is_licenced = False


password = '123'
username = 'yaseen'


if password and username:
    print("you are old enough to drive!")
elif is_licenced:
    print("you can drive now!")
else:
    print("you are not of age!")

print("okokok")


# Falsy Values in python

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(set()))


# Truthy Values in python

print(bool(1))
print(bool(-10))
print(bool("hello"))
print(bool(" "))      # space is truthy
print(bool([0]))      # list with one item
print(bool({"a": 1}))
