import inflect

def main():
    names = get_names()
    adieu(names)

def get_names():
    names = ()
    while True:
        try:
            names += (input("Name: "), )
        except EOFError:
            print()
            return names


def adieu(names):
    p = inflect.engine()
    print("Adieu, adieu, to", p.join(names))

main()
