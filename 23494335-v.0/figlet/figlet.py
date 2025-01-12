import pyfiglet
import sys

def main():
    argv_len = len(sys.argv)
    if argv_len != 1 and argv_len != 3:
        sys.exit(1)

    ft = ''
    if argv_len == 3:
        if sys.argv[1] not in ["-f", "--f"]:
            sys.exit(1)
        if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
            sys.exit(1)
        ft = sys.argv[2]

    str = input("Input: ")
    print(pyfiglet.figlet_format(str, font=ft))


main()
