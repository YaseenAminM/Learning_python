# return
def sum(num1, num2):
    def another_function(num1, num2):
        return num1 + num2
    return another_function(num1, num2)

# Should do one thing really well.
# Should return something

# total = sum(4, 5)
# print(total)
# print(sum(10, total))


total = sum(1, 1)
print(total)
