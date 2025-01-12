def main():
    dict = get_grocery_list()
    print()
    print_dict(dict)

def get_grocery_list():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
            try:
                grocery_list[item] += 1
            except KeyError:
                grocery_list[item] = 1
        except EOFError:
            return grocery_list

def print_dict(dict):
    for item in sorted(dict):
        print(dict[item], item)

main()
