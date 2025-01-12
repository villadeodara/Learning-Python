def convert(str):
    smile_words = str.split(":)")
    smile_emoji_str = '🙂'.join(smile_words)
    sad_words = smile_emoji_str.split(":(")
    emoji_str = '🙁'.join(sad_words)

    print(emoji_str)

def main():
    str = input()
    convert(str)

main()
