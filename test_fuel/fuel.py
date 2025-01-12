def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

def convert(fraction):
    norm, denom = fraction.split("/")
    try:
        x = int(norm)
        y = int(denom)
    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError

    return round(x / y * 100)

if __name__ == "__main__":
    main()
