#!/usr/bin/env python3
my_list = ["192.168.0.5", 5060, "UP"]
#ip addy
print("the first item in the list (IP): " + my_list[0] )
#port number
print("the second item in the list (port): " + str(my_list[1]))
#port state
print("the third item in the list (state): " + my_list[2])

new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

print("When I ssh into ip address " + new_list[3] + " or " + new_list[4] + " I am unable to ping ports " + str(new_list[0]) + "," + new_list[1] + ", or" + str(new_list[2]))

print(f"when I {new_list[5]} into ip address {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]} or {new_list[2]}")
