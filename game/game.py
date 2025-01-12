import random

def main():
    level = get_positive_number("Level: ")
    expected = random.randint(1, level)
    while True:
        guess = get_positive_number("Guess: ")
        if guess > expected:
            print("Too large!")
        elif guess < expected:
            print("Too small!")
        else:
            print("Just right!")
            break


def get_positive_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                continue
            else:
                return value
        except:
            pass

main()
