import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        num_tries = 0
        prompt = str(x) + " + " + str(y) + " = "
        expected = x + y
        while num_tries < 3:
            try:
                result = int(input(prompt))
                num_tries += 1
            except:
                pass
            if result == expected:
                score += 1
                break
            else:
                print("EEE")
        if num_tries == 3:
            print(prompt, expected)
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
            else:
                return level
        except ValueError:
            pass



def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)



if __name__ == "__main__":
    main()
