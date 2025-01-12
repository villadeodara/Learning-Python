def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not s[0].isalpha or not s[1].isalpha():
        return False
    seen_number = False
    for c in s:
        if not c.isalnum():
            return False
        if c.isnumeric():
            if not seen_number and int(c) == 0:
                return False
            seen_number = True
        elif seen_number:
            return False
    return True


main()
