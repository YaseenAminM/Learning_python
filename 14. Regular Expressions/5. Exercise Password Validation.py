# Exercise Password Validation
import re


# Regex patter for the password generator
pattern = re.compile(
    r"^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[$%#@])[a-zA-Z0-9$%#@!_-]{8,}(?<=[0-9])$")
stringData = "yaseen#02"


a = pattern.search(stringData)

print(a)
