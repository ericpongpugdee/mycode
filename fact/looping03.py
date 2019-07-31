#!/usr/bin/env python3
# this library allows us to generate uuid values
import uuid

howmany = int(input('how many uuids should be generated? '))

print('generating uuids...')

#range is required because an int cannot be looped 

for rando in range(howmany):
    #range(howmany) with howmany=4 will generate 1, 2, 3, 4 to run the function 4X
    #uuid is a function uuid4 is an option of uuid
    print( uuid.uuid4())

