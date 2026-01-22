# Creating Our Own Objects

class PlayerCharater:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def player_details(self):
        print(f"Player Name : {self.name}, Player Age : {self.age}")


player1 = PlayerCharater("Yaseen", 26)
player2 = PlayerCharater("Ahsan", 27)

# print(player1.name)
# print(player2.name)

player1.player_details()
player2.player_details()
