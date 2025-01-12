from datetime import date, timedelta
import inflect
import re
import sys

def main():
    date_str = input("Date of Birth: ")
    try:
        year, month, day = get_date(date_str)
        birthday = date(year, month, day)
        delta = date.today() - birthday
        p = inflect.engine()
        print(p.number_to_words(delta.days*24*60, andword="").capitalize(), "minutes")
    except:
        sys.exit("Invalid date")

def get_date(date_str):
    if matches := re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", date_str):
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
        return (year, month, day)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
