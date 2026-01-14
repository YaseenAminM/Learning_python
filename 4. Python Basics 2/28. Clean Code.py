# Clean Code

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(51))

# Clean Code
def is_odd_or_even(num):
    return "Even" if num % 2 == 0 else "Odd"


print(is_odd_or_even(2))
print(is_odd_or_even(3))
