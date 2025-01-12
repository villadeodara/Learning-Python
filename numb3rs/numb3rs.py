import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip):
        for group in matches.groups():
            number = int(group)
            if number < 0 or number > 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
