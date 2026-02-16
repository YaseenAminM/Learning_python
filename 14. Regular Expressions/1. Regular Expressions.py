# 1. Regular Expressions


import re


# pattern = re.compile("this")
pattern = re.compile("search this inside of this text please.")
string = "search this inside of this text please."

# print("search" in string)

# a = re.search("thIs", string)
# a = re.search(pattern, string)

# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())


b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(b)
print(c)
print(d)
