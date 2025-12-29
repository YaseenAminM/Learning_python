# Exercise Password Checker


user_name = input("Username? : ")
user_password = input("Password? : ")
length_user_password = len(user_password)

print(
    f"Password {user_password[0:int(length_user_password / 2)]}{"*" * int(length_user_password / 2)} is {length_user_password} letter long.")
