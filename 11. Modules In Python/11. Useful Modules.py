# 11. Useful Modules


from collections import Counter, defaultdict, OrderedDict

###############################################
# Counter

# Counter of numbers in the list
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]
# print(Counter(li))


# counting the character in the given list
sentence = "blah blah blah thinking abount python"
charCount = Counter(sentence)
# print(charCount)

# counting the words in the list
sentence = "blah blah blah thinking abount python"
wordCount = Counter(sentence.split(" "))
# print(wordCount)

###############################################
# Defaultdict

# dictionary = defaultdict(int, {"a": 1, "b": 2})
dictionary = defaultdict(lambda: "element does exist.", {"a": 1, "b": 2})

# print(dictionary['c'])
# print(dictionary['a'])

###############################################
# OrderedDict : order matters
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2
print(d == d2)
