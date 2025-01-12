def main():
    year, month, day = get_date()
    print(f"{year}-{month:02}-{day:02}")

def get_date():
     months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

     while True:
        date = input("Date: ")
        try:
            m, d, y = date.split(sep="/")
            month = int(m)
            day = int(d)
            year = int(y)
        except:
            try:
                m, d_comma, y = date.split()
                m = m.lower().title()
                if m in months:
                    month = months.index(m) + 1
                else:
                    continue
                d, _= d_comma.split(",")
                day = int(d)
                year = int(y)
            except:
                continue
        if not 1 <= month <= 12:
            continue
        if not 1 <= day <= 31:
            continue
        return year, month, day


main()
