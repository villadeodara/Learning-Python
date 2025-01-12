def greeting(s):
    s = s.strip().lower()
    if s.startswith("hello"):
        print("$0")
    elif s.startswith("h"):
        print("$20")
    else:
        print("$100")

def main():
    s = input("Greeting: ")
    greeting(s)

main()
