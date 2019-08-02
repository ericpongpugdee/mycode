#!/usr/bin/env python3
import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n****************Details of interfaces - ' + i +' ************************')
    try:
        # print(netifaces.ifaddresses(i))
        print('MAC: ', end='') #this print statement will always print MAC without an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # print the mac address
        print('IP: ', end='') #this print statement will always print IP witout an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # print the ip address
    except:  # this is a new line
        print('could not collect adapter info') # print an error message
