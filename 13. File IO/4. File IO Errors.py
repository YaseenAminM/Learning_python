# 4. File IO Errors

try:
    with open("sad.txt", mode="r") as my_file:
        text = my_file.read()
        print(text)
# except Exception as err:
except FileNotFoundError as err:
    print("file does not exist")
    raise err
except IOError as err:
    print("IO Error")
    raise err
