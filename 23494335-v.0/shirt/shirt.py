from PIL import Image, ImageOps
import os
import sys

def main():
    check_args()
    add_shirt()

def check_args():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    _, ext1 = os.path.splitext(sys.argv[1])
    _, ext2 = os.path.splitext(sys.argv[2])
    if ext1 != ext2:
        print("Input and output have different extensions")
        sys.exit(1)
    if ext1.lower() not in [".jpg", ".jpeg", ".png"]:
        print("Invalid input")

def add_shirt():
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        print("Cannot find shirt.png")
        sys.exit(1)

    try:
        with Image.open(sys.argv[1]) as im:
            im_fit = ImageOps.fit(im, shirt.size)
            im_fit.paste(shirt, shirt)
            im_fit.save(sys.argv[2])
    except FileNotFoundError:
        print("Error opening before image", sys.argv[1])
        sys.exit(1)
    except OSError:
        print("Error converting to output")
        sys.exit(1)
    shirt.close()

main()

