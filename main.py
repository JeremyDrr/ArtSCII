from PIL import Image

# From lighter to darker
ascii_char = ' .:-=+*#%@'

with Image.open("spongebob.png") as image:
    image = image.resize((500, 500))

    for y in range(image.height):
        line = ""
        for x in range(image.width):
            # Get the pixel on the RGB format
            rgb = image.getpixel((x, y))
            # Mean of each channel to make a gray nuance
            grey = sum(rgb) // len(rgb)
            # Cross-multiplication to get the index
            index = grey * 9 // 255
            line += ascii_char[index] + "  "
        print(line)

