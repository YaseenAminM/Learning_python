# Private vs Public Variables

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

print((1, 2, 3, 1).count(1))
print(len((1, 2, 3, 1)))

player1.name = "!!!!!"
player1.speak = "BOOOO"

print(player1.speak)
