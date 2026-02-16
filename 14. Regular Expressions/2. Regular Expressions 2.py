# Regular Expressions 2
import re

pattern = re.compile(r'([a-zA-Z]).([a])')

string = 'yaseen@gmail.com'

a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)

print(a.group())
