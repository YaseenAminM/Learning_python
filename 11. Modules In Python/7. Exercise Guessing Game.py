# Exercise Guessing Game
import random
randNum = random.randint(1, 10)
while True:
    try:
        userNum = int(input("Guess the number(1~9)? : "))
        if randNum == userNum:
            print("You'r correct")
            break
        else:
            print("You'r incorrect")
    except Exception as err:
        print(f"ERROR: {err}")
