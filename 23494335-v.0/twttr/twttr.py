def main():
    twttr()

def twttr():
    str = input("Input: ")
    print("Output: ", end="")
    for c in str:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            continue
        print(c, sep="", end="")
    print()

main()
