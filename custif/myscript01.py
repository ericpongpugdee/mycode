#!/usr/bin/env python3

print("what should I have for lunch today?")

wallet = input("what is in my wallet? ")

if wallet == 'cc':
    print("Anything I want")
elif float(wallet) >= 20:
    print("Perhaps cheesecake factory?")
elif float(wallet) > 5:
    print("how about a nice salad")
elif float(wallet) <= 5:
    print("better hit the atm")

else:
    print("I have lost my appetite")
