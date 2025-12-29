# Formatted Strings

# "Yaseen"
# "Amin"

name = "Yaseen"
age = 26
print('Hi, ' + name + ". You are " + str(age) + " years old")
print(f"Hi, {name}. You are {age} years old")
print("Hi, {}. You are {} years old".format("Yaseen", 26))
print("Hi, {name}. You are {age} years old".format(name="Yaseen", age=26))
print("Hi, {0}. You are {1} years old".format(name, age))
print("Hi, {new_name}. You are {new_age} years old".format(
    new_name="Amin", new_age=51))
