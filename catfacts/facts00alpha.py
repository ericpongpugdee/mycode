#!/usr/bin/env python3
'''Alta3 research | author: rzfeeser@alta3.com '''

#imports always go at the top of yuour code
import requests

def main():
    '''run time code '''
    #create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    #display the methods available to our new object
    print ( dir() )
main()

