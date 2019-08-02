#!/usr/bin/env python3
'''Alta3 research | author: rzfeeser@alta3.com '''
#imports always go at the top of yuour code
import requests
def main():
    '''run time code '''
    #create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')
    
    ## cat is our iterable -- that just means it will take on the values found within
    ## r.json()['all'], one after the next -- which happens to be a dictionary
    ## the code within the loop says 'from that single dictionary
## print the value associated with text
    for catfact in r.json()['all']:
        print(catfact.get('text'))   # the .get() method returns NONONE if key not found
main()

