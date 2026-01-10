# enumerate()


# for i, char in enumerate("Yaseen Amin Maredia"):
#     print(i, char)


for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f"index of 50 is: {i}")
