import sys
import csv
import tabulate

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    try:
        students = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for student in reader:
                name = student["name"]
                last, first = name.strip().split(",")
                students.append({"first": first.strip(), "last": last.strip(), "house":student["house"]})

    except FileNotFoundError:
        print("Could not read", sys.argv[1])
        sys.exit(1)

    open(sys.argv[2], "w")
    with open(sys.argv[2], "a") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)

main()
