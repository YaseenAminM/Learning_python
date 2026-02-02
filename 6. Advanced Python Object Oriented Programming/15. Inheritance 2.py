# Inheritance

# Users:
class User:
    def sign_in(self):
        print("Logged In")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(Wizard):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left-{self.num_arrows}")

# wizard1 = Wizard("")


archer1 = Archer("yaseen", "50")
archer2 = Archer("ali", "55")
archer1.attack()

# print(isinstance(isinstance, class))
print(isinstance(archer1, Archer))
print(issubclass(Wizard, User))
print(issubclass(Archer, Wizard))
