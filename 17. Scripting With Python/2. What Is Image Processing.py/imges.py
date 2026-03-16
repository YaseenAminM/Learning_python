from PIL import Image, ImageFilter
from pathlib import Path

img = Image.open(f"{Path(__file__).parent}/pokedex/Pokedex/pikachu.jpg")
# img.show()
print(img.size)
print(img.mode)


# print(dir(img))

# ######################################
# FILTER IMAGE
# filter_img = img.filter(ImageFilter.BLUR)
# filter_img.save("blur.png", 'png')


# filter_img = img.filter(ImageFilter.SMOOTH)
# filter_img.save("smooth.png", 'png')


# ######################################
# CONVERT FORMAT
# 1	1-bit pixels, black and white
# L	8-bit pixels, Grayscale
# P	8-bit pixels, mapped to any other mode using a color palette
# RGB	3×8-bit pixels, true color
# RGBA	4×8-bit pixels, true color with transparency mask

# convert_img = img.convert("RGBA")
# convert_img.save("grey.png", 'png')


filter_img = img.convert("RGBA")
# crooked_img = filter_img.rotate(180)

resize_img = filter_img.resize((300, 300))

resize_img.save("grey.png", 'png')
