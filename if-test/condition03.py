#!/usr/bin/env python3
# Alta3 research || author RZFeeser@alta3.com
#Check hostname against expected value

import random

#collect user input
hostname = input('what value should we set for hostname?')
#notice how the next line was changed
#here we use str.lower() methd to return a lowercase string
if hostname.lower() == "mtg":
    print("i hostname was found to be mtg")
    print('hostname matches expected config')
else: 
    print('does not match get out!')

rng= random.randint(1,999)
print("RNG said", rng)

##always print out to the user

print('exiting the script')


