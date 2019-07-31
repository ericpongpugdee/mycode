#!/usr/bin/env python3
# open file
dnsfile = open("dnsservers.txt")
# create list of lines
dnslist = dnsfile.readlines()
# loop over lines
for svr in dnslist:
    # print and end without a newline
    print(svr, end="")
    # svr is declaring the content of dnslist a variable and print it
    # end="" means back space after each items to delete extra lines. without it the list will come back double space
# close your file
dnsfile.close()
