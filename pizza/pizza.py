import sys
import csv
import tabulate

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    try:
        table = []
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)

        print(table)
        print(tabulate.tabulate(table, "firstrow", tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

main()
