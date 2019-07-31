#!/usr/bin/env python3
import sys

def main():
    print("What should I have for lunch today?") # moved inside of function
    wallet = input("What is in my wallet? ")     # moved inside of function
    if wallet == 'cc':
        print("Anything I want")
        sys.exit()  # <-- this was added so that 'cc' is not run against try statement
    try:
        wallet = float(wallet) # converting wallet into a float AFTER it is checked against 'cc' as a string
    except ValueError:
        print("That is not valid input") # message printed on user failure
        sys.exit() # exits python script on user failure
    if float(wallet) >= 20:
        print("Perhaps cheesecake factory?")
    elif float(wallet) > 5:
        print("how about a nice salad")
    elif float(wallet) <= 5:
        print("better hit the atm")
    else:
        print("I have lost my appetite")

main()
