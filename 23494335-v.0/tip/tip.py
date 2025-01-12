def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    first, second = d.split("$")
    return float(second)


def percent_to_float(p):
    first, second = p.split("%")
    return float(first)*0.01

main()
