import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"src=\"https?://(?:www\.)?youtube.com/embed/(\w+)\"", s):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        print(None)
        sys.exit(0)

if __name__ == "__main__":
    main()
