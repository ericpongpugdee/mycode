#!/usr/bin/env python3
import netifaces

print(netifaces.interfaces())
for i in netifaces.interfaces():
     print('\n****************Details of interfaces - ' + i +' ************************')
    # print(netifaces.ifaddresses(i))
     print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # print the mac address
     print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # print the ip address
