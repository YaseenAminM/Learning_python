# @classmethod and @staticmethod

class PlayerCharater:
    # Class object Attribute
    membership = True

    def __init__(self, name="anonymous", age=0):
        if (age > 18):
            self.name = name  # attribute
            self.age = age

    def run(self):
        print(f"my name is {self.name}")

    def shout(self):
        print(f"my name is {self.name}")

    def player_details(self):
        print(f"Player Name : {self.name}, Player Age : {self.age}")

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


player1 = PlayerCharater("Yaseen", 26)

# player1.player_details()


print(player1.adding_things(1, 2))
