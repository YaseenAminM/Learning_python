# filter()
my_list = [1, 2, 3]


def multiply_by_2(num):
    return num * 2


def check_odd(num):
    return num % 2 != 0


new_list = list(filter(check_odd, my_list))
print(new_list)
