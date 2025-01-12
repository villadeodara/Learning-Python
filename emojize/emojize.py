import emoji

def main():
    str = input("Input: ")
    print("Output:", emoji.emojize(str, language='alias'))

main()
