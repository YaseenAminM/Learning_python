from datetime import datetime

# Exercise Type Conversion

name = "Yaseen"
age = 26
relationship_status = "single"

relationship_status = "it's complicateds"

# print(relationship_status)


# ################################

current_year = datetime.now().year
birth_year = int(input("What year were you born? : "))
age = current_year - birth_year
print(f"You age is {age}")
