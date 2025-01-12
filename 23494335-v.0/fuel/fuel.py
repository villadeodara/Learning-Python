def main():
    percent = get_fuel("Fraction: ")

    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{percent}%")

def get_fuel(prompt):
    while True:
        try:
            norm, denom = input(prompt).split("/")
            x = int(norm)
            y = int(denom)
            if x > y or x < 0 or y < 0:
                continue
            return round(x / y * 100)
        except (ValueError, ZeroDivisionError):
            pass

main()
