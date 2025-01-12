import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.fullmatch(r"(\d{1,2}(?:\:\d{2})? (?:AM|PM)) to (\d{1,2}(?:\:\d{2})? (?:AM|PM))", s):
        start = matches.group(1)
        end = matches.group(2)
        start_converted = convert_time(start)
        end_converted = convert_time(end)
        return f"{start_converted} to {end_converted}"
    else:
        raise ValueError("Invalid Hours")

def convert_time(t):
    if matches := re.fullmatch(r"(\d{1,2})\:(\d{2}) (AM|PM)", t):
        hours = int(matches.group(1))
        mins = int(matches.group(2))
        is_pm = matches.group(3) == "PM"
    elif matches := re.fullmatch(r"(\d{1,2}) (AM|PM)", t):
        hours = int(matches.group(1))
        mins = 0
        is_pm = matches.group(2) == "PM"

    if hours > 12 or mins > 59:
        raise ValueError("Invalid hours or minutes")

    if is_pm and not hours == 12:
        hours += 12

    if not is_pm and hours == 12:
        hours = 0

    return f"{hours:02}:{mins:02}"

if __name__ == "__main__":
    main()
