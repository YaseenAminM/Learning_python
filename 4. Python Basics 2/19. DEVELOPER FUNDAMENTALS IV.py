# DEVELOPER FUNDAMENTALS IV
# - Clean
# - Readability
# - Predictability
# - Dry - don't repeat your self

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
fill = '*'
for row in picture:
    for pixel in row:
        if pixel == 1:
            print(fill, end='')
        else:
            print(' ', end='')
    print('')
