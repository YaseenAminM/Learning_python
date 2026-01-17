# nonlocal Keyword


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner : ", x)
    inner()
    print("Outer : ", x)


outer()
# 1 - start with local
# 2 - Parent local?
# 3 - Global
# 4 - Built in python function
