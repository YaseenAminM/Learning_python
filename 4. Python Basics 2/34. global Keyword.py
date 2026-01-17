# global Keyword


# scope - what variable do i have access to?

# a = 10
# def confusion(b):
#     print(b)
#     a = 90

# confusion(300)


# Example:

total = 0


def count(total):
    # global total
    total += 1
    return total


# count(total)
# count(total)
# count(total)
print(count(count(count(count(total)))))

# 1 - start with local
# 2 - Parent local?
# 3 - Global
# 4 - Built in python function
