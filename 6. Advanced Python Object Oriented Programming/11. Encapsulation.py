# Encapsulation
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"my name is {self.name}, and I and {self.age} years old.")


# PlayerCharacter Object:
player1 = PlayerCharacter("Yaseen", 26)
print(player1.name)
print(player1.age)
player1.speak()

player2 = {"name": "Yaseen", "age": 100}
print(player2["name"])
