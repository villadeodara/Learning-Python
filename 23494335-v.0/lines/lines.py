import sys

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    if not sys.argv[1].endswith(".py"):
        print("Not a python file")
        sys.exit(1)

    try:
        with open(sys.argv[1]) as file:
            number_lines = 0
            for line in file:
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue
                else:
                    number_lines += 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    print(number_lines)

main()
