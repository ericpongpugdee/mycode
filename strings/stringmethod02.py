#!/usr/bin/env python3
"""Alta research || Author: RZFeeser@alta3.com"""
def main():
    """Run-time code"""
    #create a small string
    lilstring = "Alta3 research offers classes on python coding"
    newlist = lilstring.split(" ") # this returns a list
    print(newlist)

    #creat a list of string 
    myiplist = ["192", "168", "0", "12"]
    #set singleip as the result of joining the list myuplist around the "."
    singleip = ".".join(myiplist)
    #display singleip
    print(singleip)


#call our main function
main()


