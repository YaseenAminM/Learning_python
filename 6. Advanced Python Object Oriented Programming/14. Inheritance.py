# Inheritance


# Users:


class User:
    def sign_in(self):
        print("Logged In")


class Wizard(User):
    pass


class Archer(User):
    pass


user1 = Wizard()


user1.sign_in()
