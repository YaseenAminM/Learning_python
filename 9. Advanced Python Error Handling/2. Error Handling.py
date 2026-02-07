# Error Handling
while True:
    try:
        age = int(input("What is your age? :"))
        print(age)
        age / age
    except ValueError:
        print("please enter a number")
    except ZeroDivisionError:
        print("please enter age higher than 0")
    else:
        print("Thank you!")
        break

# def get_user_age():
#     try:
#         age = int(input("Enter you age? : "))
#         return age
#     except Exception as e:
#         return e


# print(get_user_age())
