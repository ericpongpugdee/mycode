#!/usr/bin/env python3
  
import urllib.request
import re

print('what website should we search')

url = input()

print('great! so we will try to open this url ' + str(url) + 'to search for the phrase: ')

searchFor = input()

searchMe = urllib.request.urlopen(url).read().decode('utf-8')

if re.search(searchFor, searchMe):
    print('found a match! ')
else:
    print('no match ')
