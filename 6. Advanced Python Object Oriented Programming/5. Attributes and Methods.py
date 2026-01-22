# Attributes and Methods

class PlayerCharater:
    # Class object Attribute
    membership = True

    def __init__(self, name, age):
        if (self.membership):
            self.name = name  # attribute
            self.age = age

    def run(self):
        print(f"my name is {self.name}")

    def shout(self):
        print(f"my name is {self.name}")

    def player_details(self):
        print(f"Player Name : {self.name}, Player Age : {self.age}")


player1 = PlayerCharater("Yaseen", 26)
# player2 = PlayerCharater("Ahsan", 27)

# help(player1)
# print(player1.membership)
