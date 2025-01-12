import sys
import re

def main():
    s = input("Input: ")
    print(count(s))

def count(s):
    if matches := re.findall(r"\bum\b", s, flags=re.IGNORECASE):
        return len(matches)
    else:
        return 0

if __name__ == "__main__":
    main()
