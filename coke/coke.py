def main():
    amount_due = 50
    coke(amount_due)

def coke(amount_due):
    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = int(input("Insert Coin: "))
        if not coin in [5, 10, 25]:
            continue
        amount_due -= coin
    print("Change Owed:", -amount_due)

main()

