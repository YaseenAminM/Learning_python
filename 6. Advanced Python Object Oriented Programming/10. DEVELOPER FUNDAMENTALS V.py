# DEVELOPER FUNDAMENTALS V


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return self


player1 = PlayerCharacter('Yaseen', 100)

print(player1.run().name)
