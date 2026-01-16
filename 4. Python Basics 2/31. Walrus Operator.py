# Walrus Operator

# := Walrus Operaor

a = "helloooooooooooo"

if ((length := len(a)) > 10):
    print(f"too long {length} elements")

while (n := len(a) > 1):
    print(n)
    a = a[:-1]
