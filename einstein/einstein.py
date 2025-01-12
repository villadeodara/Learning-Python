def energy(mass):
    return mass * pow(300000000, 2)

def main():
    mass = int(input())
    print(energy(mass))

main()
