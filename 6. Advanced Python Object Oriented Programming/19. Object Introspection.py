# 19. Object Introspection

class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged In")


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
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


# Introspection
wizard1 = Wizard("ahsan", "magic", "ahsan@gmail.com")
archer1 = Archer("yaseen", "50")
print(dir(wizard1))
