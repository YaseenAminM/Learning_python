# 3. Error Handling 2


def sum(num1, num2):
    try:
        return num1 + num2
    # 1.
    # except TypeError:
    #     print("please enter numbers.")

    # 2.
    # except TypeError as err:
    #     print(f"please enter numbers. {err}")

    # 3.
    except (TypeError, ZeroDivisionError) as err:
        print("ooops")

        # except Exception as error_message:
        #     print(error_message)

        # print(sum('1', 2))
print(sum(1, '2'))
