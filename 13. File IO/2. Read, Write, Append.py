# 2. Read, Write, Append

# "r"   → Read only (file must exist)
# "w"   → Write only (overwrite file / create if not exists)
# "a"   → Append only (add at end / create if not exists)

# "r+"  → Read + Write (file must exist)
# "w+"  → Write + Read (overwrite file / create if not exists)
# "a+"  → Append + Read (add at end / create if not exists)

# "rb"  → Read binary
# "wb"  → Write binary
# "ab"  → Append binary

# "rb+" → Read + Write binary
# "wb+" → Write + Read binary
# "ab+" → Append + Read binary


# with open('test.txt', mode="w") as my_file:

#     # text = my_file.write(":)")
#     data = input("Enter you name? : ")
#     text = my_file.write(data)

#     print(text)

with open('sad.txt', mode="w") as my_file:
    text = my_file.write(":(")
    print(text)
