# Exercise Functions

# Problem Find the largest event number from the given list
# def higest_even(num_list):
#     print(num_list)
#     my_list = num_list.copy()
#     largest_number = 0

#     for index in my_list:
#         if index % 2 == 0 and largest_number < index:
#             largest_number = index
#     return largest_number


# print(higest_even([5, 88, 63, 444, 55, 102, 2, 931]))
# print(higest_even([1, 3, 5, 9, 11, 13, 15]))

def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    if len(evens):
        return max(evens)
    else:
        return -1


print(highest_even([5, 88, 63, 444, 55, 102, 2, 931]))
print(highest_even([1, 3, 5, 9, 11, 13, 15]))
