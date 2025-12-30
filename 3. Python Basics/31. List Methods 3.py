# List Methods 3

basket = ['a', 'b', 'c', 'd', 'e', 'f']

basket.append('a')

# Sort List
# print(basket.sort())
# print(sorted(basket))

# Copy
# new_basket = basket[:]
new_basket = basket.copy()
new_basket.append('g')
# print(new_basket)

# Reverse

basket.sort()
basket.reverse()

print(basket)
