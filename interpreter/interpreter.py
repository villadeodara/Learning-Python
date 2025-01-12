def compute(x, op, y):
    match op:
        case "+":
            value = float(x) + float(y)
        case "-":
            value = float(x) - float(y)
        case "*":
            value = float(x) * float(y)
        case "/":
            value = float(x) / float(y)
    print(f"{value:.1f}")

def main():
    x, op, y = input("Expression: ").split()
    compute(x, op, y)

main()
