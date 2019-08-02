#!/usr/bin/env python3
'''Alta3 research | author: rzfeeser@alta3.com '''
#imports always go at the top of yuour code
import requests
def main():
    '''run time code '''
    #create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')
#the .json() method will dump a json string into Pythonic data structures. cool!
    #this is much easier than using the urllib.request library
    print(r.json())
    # create 3 new lines via the escape character \n
    print("\n\n\n")

    #if we request the 'all' key, we can strip off the outside {}
    #this seems minor, but is critical if we want to parse our data
    print(r.json().get('all'))

main()




