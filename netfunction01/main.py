#!/usr/bin/env python3

""" Alta3 research || author: RZFeeser@alta3.com """

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print("Handshaking. .. ... connecting with " + coffeetime)
        # we will learn to write code that connects devices here
        for mycmds in devicecmd[coffeetime]:
            print('attempting to send command ---> ' + mycmds)
            # we will learn to write code that sends cmds to device here

# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth 1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "noshutdown"]} #data that replaces data stored in file

    print("welcome to the network device command pusher") #welcome message

    ## get data set
    print("\nData set found \n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices

# call our main function
main()



