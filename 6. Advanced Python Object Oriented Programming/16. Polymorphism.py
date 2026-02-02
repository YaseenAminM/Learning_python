# 16. Polymorphism

# Users:
class User:
    def sign_in(self):
        print("Logged In")

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        # Using the attacking method from it's parent class
        User.attack(self)
        print(f"attacking with power of {self.power}")


class Archer(Wizard):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left-{self.num_arrows}")


wizard1 = Wizard("ahsan", "magic")
archer1 = Archer("yaseen", "50")


def player_attack(char):
    char.attack()


# player_attack(wizard1)
# player_attack(archer1)


for char in [wizard1, archer1]:
    player_attack(char)
