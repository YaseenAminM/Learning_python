# 5. Exercise Translator

from translate import Translator

try:
    with open("test.txt", mode="r", encoding="UTF-8") as my_file:
        data = my_file.read()
        print(data)
        translator = Translator(to_lang="ur")
        translation = translator.translate(data)
        print(translation)
    with open("./test-ur.txt", mode="w", encoding="UTF-8") as my_file_2:
        my_file_2.write(translation)
except Exception as err:
    print(err)
finally:
    my_file.close()
