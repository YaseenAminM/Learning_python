from PIL import Image
import sys
import os

# grab first and second arguments
# print(sys.argv[1])
# print(sys.argv[2])

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exist, if not create it
if os.path.exists(output_folder):
    print("Folder exists")
else:
    os.makedirs(output_folder)

# loop through the pokedex
# save to the new folder
# covert images to png
for item in os.listdir(f"{image_folder}"):
    img = Image.open(f"./{image_folder}/{item}")
    img.save(f"./new/{item.replace('jpg', 'png')}", "PNG")
