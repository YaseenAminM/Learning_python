# Scope Rules
# Scope – what variables do I have access to?
a = 1


def parent():
    a = 10

    def confusion():
        return a
    return confusion()


# 1 - Start with local
print(parent())
# 2 - Parent local?
# 3 - Global
# 4 - built in python functions.
