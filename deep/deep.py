def check_answer(ans):
    match ans.strip().lower():
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    check_answer(ans)

main()
