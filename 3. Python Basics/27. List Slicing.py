# List Slicing
amazon_cart = ["notebooks",
               "sunglassed",
               "toys",
               "grapes"
               ]

# print(amazon_cart)
print(amazon_cart[0::2])


# greet = "Hello"
# This is not possible in the string
# greet[0] = "Z"

# This is correct with list
amazon_cart[0] = "Laptop"

# Copying the list
new_cart = amazon_cart[:]
new_cart[0] = "Gum"

print(amazon_cart)
print(amazon_cart[0::3])


print(new_cart)
