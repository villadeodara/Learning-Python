def main():
    time = input("What time is it? ")
    float_hours = convert(time)
    if 7.0 <= float_hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= float_hours <= 13.0:
        print("lunch time")
    elif 18.0 <= float_hours <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.strip().split(":")
    return float(hours) + float(minutes)/60.0


if __name__ == "__main__":
    main()
