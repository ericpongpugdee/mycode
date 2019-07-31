#!/usr/bin/env python3

ipchk = input('apply an ip address: ') #this line now ask for the user input

if ipchk =="192.168.70.1": # if a match
    print('look like the up address of the gateway was set: ' +ipchk + "this is not recommended")

elif ipchk: # if all data is provided
    print('look like the ip address was set: ' + ipchk)  # indented under if

else: # if data is not provided
    print('you did not provide input') 

    
