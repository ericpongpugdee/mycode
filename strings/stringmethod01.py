#!/usr/bin/env python3

#create a small string
lilstring = "Alta3 research offers classes on python coding"
newlist = lilstring.split(" ") # this returns a list
print(newlist)

#create a list of string
myiplist = ["192", "168", "0", "12"]
#set singleip as the result of joining the list myiplist around the "."
singleip = ".".join(myiplist)
# display singleip
print(singleip)

