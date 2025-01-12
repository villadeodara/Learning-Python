def main():
    camel_str = input("camelCase ")
    snake(camel_str)

def snake(str):
    for c in str:
        if (c.isupper()):
            print("_", c.lower(), sep="", end="")
        else:
            print(c, end="")
    print()

main()
