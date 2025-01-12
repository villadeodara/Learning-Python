import sys
import json
import requests

def main():
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
    elif len(sys.argv) != 2:
        sys.exit(1)
    else:
        try:
            n = float(sys.argv[1])
        except:
            print("Command-line argument is not a number")
            sys.exit(1)
        if n < 0:
            sys.exit(1)

    price = get_bitcoin_price()
    amount = n * price
    print(f"${amount:,.4f}")

def get_bitcoin_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    bpi = o["bpi"]
    usd_bpi = bpi["USD"]
    return usd_bpi["rate_float"]

main()
