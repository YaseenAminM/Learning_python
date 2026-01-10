# Exercise Logical Operators


is_magician = False
is_expert = False

# Chek if magician AND expert : "You are a master magician"
if is_magician and is_expert:
    print("You are a master magician")

# Check if magician but not expert: "at least you're getting there"

elif is_expert or (is_expert):
    print("at least you're getting there")
elif not is_expert:
    print("You need magic powers")
