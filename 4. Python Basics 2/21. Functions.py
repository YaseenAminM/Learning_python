# Functions

# DRY
def say_hello():
    print("helllllooooo")


say_hello()
say_hello()

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# show_tree() # Error


def show_tree():
    fill = '*'
    for row in picture:
        for pixel in row:
            if pixel == 1:
                print(fill, end='')
            else:
                print(' ', end='')
        print('')


show_tree()
show_tree()
