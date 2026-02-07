# Error Handling 3

while True:
    try:
        age = int(input("What is your age? :"))
        print(age)
        10 / age
        raise ValueError("Hey cut it out!")
    except ZeroDivisionError:
        print("please enter age higher than 0")
        break
    else:
        print("Thank you!")
        break
    finally:
        print("ok i am finally done")
    print("can you hear me?")
