from PIL import Image
import sys


def decompress(width, height, bytes):
    image = Image.new("1", (width, height))

    col = 0
    row = 0
    for byte in bytes:
        color = (byte & 128) >> 7
        count = byte & ~128
        for i in range(count):
            image.putpixel((row, col), color)
            row += 1
        if not row % width:
            col += 1
            row = 0
    return image


with open(sys.argv[1], "rb") as file:
    width = int.from_bytes(file.read(2), "little")
    height = int.from_bytes(file.read(2), "little")

    image = decompress(width, height, file.read())
    image.save(sys.argv[2], "bmp")
